.. _tf2_v_characterandrig:

Character and Rig
-----------------

| :ref:`tf2_v_characterandrig_method1` is the best of these, as the work is already done. `Hisanimations <https://youtube.com/c/hisanimations>`_ from the `TF2 Blender Discord server <https://discord.gg/zHC2gJW>`_ has already made a fully working Character Ports file that you can use for yourself. His `YouTube video <https://youtu.be/0DMz-n1LSII>`_ explains what it is and how to use it. If you have questions or need help with this port, you can ask on the `Discord server <https://discord.gg/zHC2gJW>`_. Using this method is recommended in most cases, but if you intend on animating, then :ref:`tf2_v_characterandrig_method2` is slightly better, as it gives better FPS when working with keyframes, but you lose out on the ease of use and the support.
| :ref:`tf2_v_characterandrig_method2` is to get the stuff directly from the in-game files. This method is recommended for animation work where you need the maximum possible performance. You can still animate completely fine with :ref:`tf2_v_characterandrig_method1`, but this one just gives a slightly higher FPS number.
| :ref:`tf2_v_characterandrig_method2` requires a functioning copy of Team Fortress 2 and a recent copy of Blender. You don't need a copy of the game for method 1. 

.. note::

    | There is also a difference in quality for these methods. Method 1 uses the characters obtained from Source Filmmaker, which has higher quality models intended for animation work. Method 2 will use the models present in the game, which are of lesser quality. If you want to use Method 2, and also want the higher quality models, then the process for the files is the same, except they must be obtained from ``tf_movies`` from SFM.
    | Method 2 having a higher performance compared to Method 1 isn't because of the difference in the models used, but also because Method 1 has extra features packed into it and actively running scripts. The performance is small, though, so unless you REALLY need that small gain because of a weaker computer or if you're animating a very complex scene, just use Method 1. A funny thing is, if you play an Animation with the Armature selected, it straight up halves the performance, so do make sure that nothing is selected when playing something back.

.. _tf2_v_characterandrig_method1:

Method 1 (Recommended)
^^^^^^^^^^^^^^^^^^^^^^

| Watch the `Hisanimations TF2 Blender Character port <https://youtu.be/7rH6_eq-I0c>`_ video and follow the instructions.

.. _tf2_v_characterandrig_method2:

Method 2 (Alternate)
^^^^^^^^^^^^^^^^^^^^

.. _tf2_v_characterandrig_method2_summary:

Summary of Method 2
"""""""""""""""""""

*    Download GCFScape, and SourceIO. Install SourceIO as an Add-on into Blender (This step is only necessary for first time use).
*    Use GCFScape to extract the necessary class files from ``tf2_misc_dir.vpk`` into a folder of your choice (This step is only necessary for first time use).
*    Import the ``.MDL`` of the character from :guilabel:`File` > :guilabel:`Import` > :guilabel:`Source Engine Assets` > :guilabel:`Source Model (.mdl)`.
*    Clean up the import by renaming the appropriate files and deleting any extra Objects that aren't required.

.. _tf2_v_characterandrig_method2_detailed:

Full Guide of Method 2
""""""""""""""""""""""

*    Download `GCFScape <https://nemstools.github.io/pages/GCFScape-Download.html>`_, and `SourceIO <https://github.com/REDxEYE/SourceIO>`_. Instructions for installing are under :ref:`installingprograms`.
*    Go to ``[game_directory] / tf`` and open the file called ``tf2_misc_dir.vpk``. It should open through GCFScape.
*    This next step will add ``2.5 GB`` to your game folder size, so make sure you're not low on space. Extract the ``Models`` folder into ``[game_directory] / tf``. Don't try to Drag and Drop as it's extremely laggy and buggy. Right click the folder and click :guilabel:`Extract` so you may extract it. Once done, close GCFScape.
*    In Blender, go into :guilabel:`File` > :guilabel:`Import` > :guilabel:`Source Engine Assets` > :guilabel:`Source Model (.mdl)` (Make sure SourceIO is installed).
*    Go to ``[game_directory] / tf / models / player``. Here you'll find a bunch of files that have the names of the TF2 mercenaries, such as heavy.mdl or spy_animations.mdl, and so on. Only focus on the one that doesn't have animations in the name, as the other files are for the :ref:`tf2_v_animations` section.
*    For the class you want to import, click the ``(class).mdl``. If you want the imported model to be compatible with taunts or animations (the process of which is explained further down the page), then make sure to set the :guilabel:`World scale` to 1.
*    If everything was done right, you should now have the model in Blender with a fully working rig and textures. Make sure to use Material Preview to confirm that the textures are functional.

.. note::

    | This process is identical to that used in :ref:`tf2_v_prop_method2` of the :ref:`tf2_v_prop` Section, but needs less files to be extracted. As for why, we don't know. SourceIO is very mysterious.

| If you used TF2's in-game files, then inside GCFScape when you're extracting the files from ``tf2_misc_dir.vpk``, you might have noticed that similar files were also under ``models / player / hwm``. The difference between these files and the ones inside ``models / player`` is only of the mouth supposedly having HWM properties. HWM, or HardWare Morph System, is used by VALVe for facial reflexes and stuff. But according to Hisanimations, they aren't used in TF2, despite their files being present. Whether you use files under ``models / player`` or ``models / player / hwm``, won't matter. Other than the mouth, both have the exact same mesh and their quality will be the same.
    | Again, as mentioned earlier, if you want better quality models, you need to get the files from ``tf_movies`` from SFM, or just use :ref:`characterandrig_method1` for the highest quality models and ease of use.

