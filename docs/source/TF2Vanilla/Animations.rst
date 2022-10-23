.. _tf2_v_animations:

Animations
----------

| Regardless of what method you use to import the TF2 characters and their appropriate rigs, be it the Hisanimations port, or the TF2 in game models, or the SFM models, all use the same method for applying in-game animations (But for the Hisanimations port, you do have to make sure you get the one that's compatible with taunts. That one is available under the ``#community-ports`` channel of the `TF2 Blender Discord server <https://discord.gg/zHC2gJW>`_). There's no other method hence only one method is listed.
| This is a bit long and tedious so, make sure to follow every step carefully, but at least you won't have to do these animations yourself from scratch. The method works.
| 

.. note::

    | Not all animations from TF2 can be imported with ease. It depends on which specific animation you want to import. Some animations in TF2 are additive, instead of independent, meaning that you need a base animation and the new animation adds on top of it. For example, to bring in the animation of shooting the shotgun, you first need to have the idle animation of that shotgun brought in.
    | This is possible in SFM. However, in Blender, a script is required. It's currently being developed by Hisanimations and not ready right now. 

.. _tf2_v_animations_method1:

Method
^^^^^^

.. _tf2_v_animations_method1_summary:

Summary of Method
"""""""""""""""""

*    Download GCFScape, Blender Source Tools, and Crowbar. Install Blender Source Tools as an Add-on into Blender (This step is only necessary for first time use).
*    Using GCFScape, extract the necessary class files from ``tf2_misc_dir.vpk`` into a folder of your choice (This step is only necessary for first time use).
*    Open the appropriate ``.MDL`` file in Crowbar and Decompile it into another folder.
*    Use Blender Source Tools to import the ``.QC`` file.
*    Remove or hide any unnecessary objects such as the hitbox or extra LOD models.

.. _tf2_v_animations_method1_detailed:

Full Guide of Method
""""""""""""""""""""

*    Download `GCFScape <https://nemstools.github.io/pages/GCFScape-Download.html>`_, `Crowbar <https://steamcommunity.com/groups/CrowbarTool>`_, and `Blender Source Tools <https://developer.valvesoftware.com/wiki/Blender_Source_Tools>`_. Instructions for installing are under :ref:`installingprograms`.
*    Go to ``[game_directory] / tf`` and open the file called ``tf2_misc_dir.vpk``. It should open through GCFScape.
*    From GCFScape, extract the ``models`` folder to ``[game_directory] / tf``. If you've already done this step from previous guides, there's no need to do it again. Otherwise, make sure you have space, as this step will add 2.5 GB to your TF2 folder.
*    Close GCFScape. Go to the folder you just extracted, which is ``models``, and go to the ``player`` folder. Copy ``(class)_animations.mdl`` to another location, preferably a new folder. This is the file that holds almost all animation data for that specific class.
*    Repeat the process for the ``.MDL`` present in ``models / workshop / player / animations``. Just in case the specific animation can't be found in that first ``.MDL`` file, we'll get the remaining ones from here too.
*    Open Crowbar, and go to the :guilabel:`Decompile` tab. For the ``MDL`` file, select the ``.MDL`` from the files you just extracted through GCFScape.
*    For the Output Folder, make a new folder or choose an existing one to Decompile to.
*    You don't need to change any settings, click :guilabel:`Decompile` in the bottom left. If done right, the folder should have a very large amount of ``.SMD`` files.
*    Finally, In Blender, click on the specific skeleton you want to apply an animation to (You do have to import the Character first. You can't just bring the animation into an empty scene).
*    After that, go into :guilabel:`File` > :guilabel:`Import` > :guilabel:`Source Engine (.smd, .vta, .dmx, .qc)`.
*    Go to the folder where Crowbar Decompiled the files. In there you should find multiple files, all with a lot of names. Find the one that you're after, and import it.
*    If everything was done right, the Timeline in Blender should adjust itself and by pressing play, the Animation should be visible.

.. note::

    | In some cases, you may find two identically named files, one name starting with ``taunt_`` and the other name starting with ``layer_taunt_``. These are different files. As of writing, it is uncertain which is the one to use but, if one file doesn't give the wanted results, try the other. Also, not every animation is guaranteed to work, even if it's not an Additive one.
    | Animations are designed to be played back at 30fps or 24fps. You can use the NLA Editor to change the speed of the animation.
    
