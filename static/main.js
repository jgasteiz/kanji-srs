(function () {
    const LEVEL_CONTAINER_EL = document.getElementById('level-list'),
        KANJI_CONTAINER_EL = document.getElementById('kanji-list'),
        TEMPLATES = document.getElementById('templates');

    let LEVEL_DATA;

    /**
     * Initialise the app:
     *
     * - Show the Level container.
     * - Hide the Kanji container.
     * - Load the levels from the API or from memory.
     */
    function init() {
        LEVEL_CONTAINER_EL.innerHTML = "";
        KANJI_CONTAINER_EL.innerHTML = "";
        LEVEL_CONTAINER_EL.classList.toggle("d-none", false);
        KANJI_CONTAINER_EL.classList.toggle("d-none", true);

        // If the level data has not been loaded yet, load it.
        if (LEVEL_DATA === undefined) {
            fetch("/levels/")
                .then((response) => response.json())
                .then((data) => LEVEL_DATA = data)
                .then(() => _loadLevels(LEVEL_CONTAINER_EL));
        } else {
            _loadLevels(LEVEL_CONTAINER_EL);
        }
    }

    /**
     * Load the levelData in the given container.
     *
     * @param containerEl
     * @private
     */
    function _loadLevels(containerEl) {
        LEVEL_DATA.forEach(level => _loadLevel(level, containerEl))
    }

    /**
     * Load a level in the given container.
     *
     * @param level
     * @param containerEl
     * @private
     */
    function _loadLevel(level, containerEl) {
        const levelElement = TEMPLATES.querySelector('[data-id="level-template"]').cloneNode(true),
            buttonGroup = levelElement.querySelector('[data-id="level-groups"]');

        levelElement.querySelector('[data-id="level-name"]').innerText = `${level.name.toUpperCase()} Kanji`;
        containerEl.append(levelElement);

        level.groups.forEach(group => _loadGroup(group, buttonGroup));
    }

    /**
     * Load a level group in the given list element.
     *
     * @param group
     * @param buttonGroup
     * @private
     */
    function _loadGroup(group, buttonGroup) {
        const groupButton = TEMPLATES.querySelector('[data-id="group-template"]').cloneNode(true);
        groupButton.innerText = `Group ${group.index} (${group.kanji_list.length} kanji)`;
        groupButton.addEventListener("click", () => {
            _loadKanjiList(group.index, group.kanji_list)
        });
        buttonGroup.append(groupButton);
    }

    /**
     * Changes "level browsing" mode to "kanji browsing" and load the given
     * list of kanji in the global KANJI_CONTAINER_EL.
     *
     * @param groupName
     * @param kanjiList
     * @private
     */
    function _loadKanjiList(groupName, kanjiList) {
        const groupNameEl = document.createElement("h1");
        groupNameEl.innerText = `Group ${groupName}`;
        KANJI_CONTAINER_EL.append(groupNameEl);

        // Hide levels, show kanji
        LEVEL_CONTAINER_EL.classList.toggle("d-none", true);
        KANJI_CONTAINER_EL.classList.toggle("d-none", false);

        kanjiList.forEach((kanji) => _loadKanji(kanji));

        // Exit button
        const back = document.createElement("button");
        back.innerText = "Back";
        back.className = "btn btn-primary";
        back.addEventListener("click", () => init())
        KANJI_CONTAINER_EL.append(back);
    }

    /**
     * Load a single kanji in the global KANJI_CONTAINER_EL.
     *
     * @param kanji
     * @private
     */
    function _loadKanji(kanji) {
        const kanjiEl = TEMPLATES.querySelector('[data-id="kanji-template"]').cloneNode(true);
        kanjiEl.querySelector('[data-id="kanji"]').innerText = kanji.kanji;
        kanjiEl.querySelector('[data-id="examples"]').innerText = kanji.examples;
        kanjiEl.querySelector('[data-id="meaning"]').innerText = kanji.meaning;
        kanjiEl.querySelector('[data-id="kun-yomi"]').innerText = kanji.kun_yomi;
        kanjiEl.querySelector('[data-id="on-yomi"]').innerText = kanji.on_yomi;
        KANJI_CONTAINER_EL.append(kanjiEl);
    }

    init();
})();
