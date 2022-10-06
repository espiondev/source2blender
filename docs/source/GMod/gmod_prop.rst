.. _gmod_prop:

Individual Props
----------------

| This section is written as a way to obtain individual props that are universally used in maps stored in Gmod files, such as Barrels. Some maps will have props that aren't used universally, and are exclusive to them. In this case it's best to just import the map, find the prop, and separate it.

.. _gmod_prop_method1:

Method
^^^^^^

.. _gmod_prop_method1_summary:

Summary of Method
"""""""""""""""""

*    Download SourceIO. Install SourceIO into Blender (This step is only necessary on first time use).
*    (Vanilla) Download GCFScape. Use GCFScape to extract the necessary files from ``garrysmod_dir.vpk`` into ``[game_directory] / garrysmod`` (This step is only necessary on first time use).
*    (Workshop and Mods) Use GMad to obtain the files of the addon or mod, and move the folders into ``[game_directory] / garrysmod`` (This step is only necessary for first time use).
*    Use SourceIO to import ``.MDL`` file of choice from the extracted folders.

.. _gmod_prop_method1_detailed:

Full Guide of Method
""""""""""""""""""""

| The process is rather simple, it only requires a bit of setup, then the importing of the prop should be doable with a few clicks.
*    Download `SourceIO <https://github.com/REDxEYE/SourceIO>`_. Install SourceIO into Blender (Installation guide listed in :ref:`installingprograms`).

| Steps for Vanilla:
*    Download `GCFScape <https://nemstools.github.io/pages/GCFScape-Download.html>`_ and install it.
*    Go to ``[game_directory] / garrysmod`` and open the file called ``garrysmod_dir.vpk``. It should open through GCFScape.
*    In GCFScape, Right Click the ``Models`` folder, click :guilabel:`Extract`, and Extract it to ``[game_directory] / garrysmod``. Don't drag and drop as it is laggy and can bug out.
*    Then in GCFScape, Extract the folder called ``Materials`` to ``[game_directory] / garrysmod`` as well.

| Steps for Workshop and Mods:
*    (Addon) Use Gmad (Instructions for how to use it are at the :ref:`gmod_gmad` Section) to obtain the files from the ``.GMA`` file. Open the newly created folder, and move all the folders inside to ``[game_directory] / garrysmod``.
*    (Mods) If it is a ``.GMA`` file, use Gmad to obtain the folders. If it is regular files, extra work isn't required. Just move the folders into ``[game_directory] / garrysmod``.

| All of that was for setting things up. Once that's completed, all you have to do for bringing a Model in is to open Blender, click :guilabel:`File` > :guilabel:`⤓ Import` > :guilabel:`Source Engine Assets` > :guilabel:`Source model (.mdl)`, and choose the ``.MDL`` file you're after inside the ``Models`` folder. It should have textures set up and everything. The above steps don't have to be repeated.
