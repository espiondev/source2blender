.. _tf2_v_prop:

Individual Props
----------------

| This section is written as a way to obtain individual props that are universally used in maps stored in the TF2 files, such as Barrels, Control Points, or Gates. Some maps will have props that aren't used universally, and are exclusive to them. These can still be obtained with both methods.
| :ref:`tf2_v_prop_method1` is the better of the two, as the work is already done. `Hisanimations <https://youtube.com/c/hisanimations>`_ has already made a fully working Props, Weapons, and Cosmetics Ports file that you can use for yourself. His `YouTube video <https://youtu.be/0DMz-n1LSII>`_ explains what it is and how to use it. If you have questions or need help with this port, you can ask on the `TF2 Blender Discord Server <https://discord.gg/zHC2gJW>`_ as he's an active member there.
| :ref:`tf2_v_prop_method1` is also significantly more space effective. The download of it takes up ``5.2 GB`` while doing it using :ref:`tf2_v_prop_method2` will add ``7.7 GB`` to your TF2 game directory.

.. _tf2_v_prop_method1:

Method 1 (Recommended)
^^^^^^^^^^^^^^^^^^^^^^

| Watch the `Hisanimations TF2 Blender Weapons, Cosmetics, and Props port <https://youtu.be/0DMz-n1LSII>`_ video and follow the instructions.

.. raw:: html
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/0DMz-n1LSII" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

.. _tf2_v_prop_method2:

Method 2 (Alternate)
^^^^^^^^^^^^^^^^^^^^

.. _tf2_v_prop_method2_summary:

Summary of Method
"""""""""""""""""

*    Download GCFScape, and SourceIO. Install SourceIO as an Add-on into Blender.
*    Use GCFScape to extract the necessary files from ``tf2_misc_dir.vpk`` and ``tf2_textures_dir.vpk`` into ``[game_directory] / tf``.
*    Use SourceIO to import ``.MDL`` file of choice from the extracted folders.

.. _tf2_v_prop_method2_detailed:

Full Guide of Method
""""""""""""""""""""

| The process is rather simple. It only requires a bit of setup, then the importing of the prop should be doable with a few clicks.
*    Download `GCFScape <https://nemstools.github.io/pages/GCFScape-Download.html>`_, and `SourceIO <https://github.com/REDxEYE/SourceIO>`_. Install SourceIO into Blender (installation guide listed in :ref:`installingprograms`)
*    Go to ``[game_directory] / tf`` and open the file called ``tf2_misc_dir.vpk``. It should open through GCFScape.
*    In GCFScape, right Click the ``Models`` folder, click :guilabel:`Extract`, and Extract it to ``[game_directory] / tf``. Don't try to Drag and Drop as it's extremely laggy and buggy. The extraction will be 2.5 GB in size so make sure you have the space for it.
*    After that, go back a step, then go into the ``Materials`` folder. Inside of this is another folder called ``Models``. Extract this to ``[game_directory] / tf`` as well.
*    Close GCFScape. Go to ``[game_directory] / tf`` and open the file called ``tf2_textures_dir.vpk``. It should open through GCFScape, just like the previous ``.VPK`` file.
*    This next step will add ``5.3 GB`` to your game folder size, so make sure you have the space for it. There should be only one folder inside, called ``Materials``. Open this, then find the ``Models`` folder. Extract this folder to ``[game_directory] / tf``. You can now close GCFScape.
| All of that was for setting things up. Once that's completed, all you have to do for bringing a Model in is to open Blender, click :guilabel:`File` > :guilabel:`⤓ Import` > :guilabel:`Source Engine Assets` > :guilabel:`Source model (.mdl)`, and choose the ``.MDL`` file you're after inside the ``Models`` folder. It should have textures set up and everything. The above steps don't have to be repeated.
