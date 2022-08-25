.. _tf2_vanilla:

Team Fortress 2 Vanilla
=======================

| Throughout this page, you'll find clickable text where a link is provided. Just click on it or right click and 'Open in new tab' to see the contents.
| Depending on the category you'll find two methods or only one. Where there are multiple methods (Such as in the :ref:`tf2_v_map` Section), the benefits and drawbacks will be listed. Places where there's only one method means that other methods just wasn't as good/worth it, or there only is one way to do it.
| It's best if you have an up-to-date copy of Team Fortress 2 installed as nearly all of these methods will be relying on obtaining files present from within the game.

.. contents:: Table of Contents
    :depth: 3


.. _tf2_v_map:

Maps and included props
-----------------------

| :ref:`tf2_v_map_method1` uses three tools, all linked in that section. This method is recommended as it makes the maps significantly easier to work with. All imported items are organized into collections and very easy to work with and customize.
| :ref:`tf2_v_map_method2` uses only one addon, called SourceIO. It's a one click solution and way easier than :ref:`tf2_v_map_method1`, but the names of objects becomes messy, and there's extra cleanup required as extra objects such as the map hitbox is also imported. It's closer in looks to TF2 as it uses its own shader, so if you want the true TF2 look, then use this. :ref:`tf2_v_map_method1` also works fine but is better suited for applying your own style or flair to your renders and animations. 
| Both methods require a fully working copy of Team Fortress 2 and a recent copy of Blender. If you are unable to get these methods to work, it is recommended to use the latest version of Blender.

.. _tf2_v_map_method1:

Method 1 (Recommended)
^^^^^^^^^^^^^^^^^^^^^^

.. _tf2_v_map_method1_summary:

Summary of Method 1
"""""""""""""""""""

*    Download BSPSource, Plumber, and Blender Source Tools. Install Plumber and Blender Source Tools as Add-ons into Blender (This step is only necessary on first time use).
*    Locate the map you wish to bring into Blender by going to ``[game_directory] / tf / maps``.
*    If necessary, Repack the ``.BSP`` file using ``EspionRepacker``.
*    Convert the ``.BSP`` file into a ``.VMF`` file using BSPSource.
*    Import the ``.VMF`` file from :guilabel:`File` > :guilabel:`Import` > :guilabel:`Plumber` > :guilabel:`Valve Map Format (.vmf)` in Blender.
*    Disable all lights except ``light_environment``, and set Color Profile from :guilabel:`Filmic` to :guilabel:`Standard`.

.. _tf2_v_map_method1_detailed:

Full Guide of Method 1
""""""""""""""""""""""

.. note::
    Always get the most recent version of a program or Add-on linked here.

| `Blender Source Tools <http://steamreview.org/BlenderSourceTools>`_, `BSPSource <https://developer.valvesoftware.com/wiki/BSPSource>`_, and `Plumber <https://github.com/lasa01/io_import_vmf/releases>`_ will be used for Method 1. The steps to install these can be seen at the :ref:`installingprograms` section. 
| Plumber was originally called io_import_vmf, and it's by the same developers. It's currently in Beta but significantly superior to io_import_vmf and that's why we've linked the page to download that instead.

| To start off, we need to make sure the map is even usable in the first place. Some maps are compressed beyond readability for BSPSource (Usually newer ones). To fix that, you need to repack it.

.. _tf2_v_fix_compressed_bsp:

Repack compressed .BSP files
""""""""""""""""""""""""""""

.. note::

    | These steps are only to be followed in case a .BSP file was too compressed for BSPSource. If you're unsure, better to do it anyways.
    | Make sure to follow the steps in the right order. 

*    Go to the releases page for `EspionRepacker <https://github.com/spy-ware/EspionRepacker/releases>`_ and download the latest version (don't download the one called Source Code).
*    For the BSPZip folder, go to ``[game directory] / bin``.
*    For the map you want to Repack, go to ``[game directory] / tf / maps`` and choose the specific ``.BSP`` file (Map file) you want to Repack.
*    The output folder is of your own choice, but make sure it's a place you can come back to easily.
*    Click on :guilabel:`Repack` to repack your file. A folder will be generated called ``out``, and within this folder will be the ``.BSP`` file, ready to use for the next steps. 

.. _tf2_v_convert_bsp_to_vmf:

Convert a .BSP to .VMF
""""""""""""""""""""""

.. important::

    You need to install `Java <https://www.java.com/download/ie_manual.jsp>`_ to run BSPSource.

*    Download `BSPSource <https://developer.valvesoftware.com/wiki/BSPSource>`_ and extract all files to a folder.
*    Open ``bspsrc.jar`` from this folder.
*    There's many options in the program. For now, just click the button for :guilabel:`Add`. From there, if you repacked a file using EspionRepacker, go to the folder where the Output file is (the one which is a ``.BSP`` file) and select it. Otherwise, go to ``[game_directory] / tf / maps`` and choose the specific map file you want to convert (these are also ``.BSP`` files).
*    Go to the :guilabel:`Other` tab in BSPSource, and enable the checkbox labelled :guilabel:`Extract Embedded Files`.
*    Once done, just click the :guilabel:`Decompile` button in the bottom right. There's no need to edit the other settings, though you're free to play around if you know what you're doing.
*    A file browser will show up for where to put the ``.VMF`` file. You can choose any location, but it's best if it's a place you can easily come back to.
*    Click on :guilabel:`Decompile`.

| Your .VMF file has now been decompiled and is in your output folder. You'll notice another folder in that location with the same name as the ``.VMF`` file. We'll use this later. If such a folder doesn't exist, then don't worry about it.

.. important::

    During the time that BSPSource is Decompiling the map, it will show logs of what it's doing. There is an ``Errors & Warnings`` box visible. This should be completely empty. If at any point something is shown in this box, then the process failed and needs to be done again. 

.. _tf2_v_importing_vmf:

Bringing The Map In
"""""""""""""""""""

| You can now import a .VMF file from the :guilabel:`File` > :guilabel:`Import` > :guilabel:`Plumber` > :guilabel:`Valve Map Format (.vmf)` button (Make sure Plumber and Blender Source Tools are installed). Browse to the location you stored your ``.VMF`` file which you Decompiled using BSPSource earlier. 
*    Make sure that in the Import settings, the game is set to Team Fortress 2. 
*    Set the Scale to be set to 0.1, and the Light Brightness set to 10. This is so the map is compatible with the Hisanimations Characters port and TF2 Collections Port.
*    In the folder space underneath the :guilabel:`Game`, type the name of the folder with the same name as the ``.VMF``. So if for example, your map file is called ``pl_pier_d.vmf`` then there should also be a folder called ``pl_pier_d``. Write ``pl_pier_d`` in that space. If you don't have such a folder, you can skip this step.
*    Then click the ``.VMF`` file, and click :guilabel:`Import`. That's it, you should have everything. 

| The installation steps are not necessary to do again. It's really just as simple as, Repack ``.BSP`` if needed, Turn into ``.VMF`` with BSPSource, Bring ``.VMF`` into Blender.
| Go to :ref:`tf2_v_finishing_touches` for advice on clean up and additional useful things to know about within Blender regarding these maps.
| If you wish to familiarize yourself with the whole process, or see an overview, a :ref:`tf2_v_map_method1_summary` is written which you can refer to.
| If any problems occur you can ask for help on the `TF2 Blender Discord server <https://discord.gg/zHC2gJW>`_.

.. _tf2_v_map_method2:

Method 2 (Alternate)
^^^^^^^^^^^^^^^^^^^^

.. _tf2_v_map_method2_summary:

Summary of Method 2
"""""""""""""""""""

*    Download SourceIO and install it as an Add-on into Blender (This step is only necessary for first time use).
*    Go to :guilabel:`File` > :guilabel:`Import` > :guilabel:`Source Engine Assets` > :guilabel:`Source Map (.bsp)` in Blender.
*    Locate the map you wish to bring into Blender under ``[game_directory] / tf / maps``.
*    Select everything by pressing A, then Shift Click an ``Empty``.
*    Press N under the 3D Viewport to open the sidebar, go to SourceIO, and click :guilabel:`Load Entity`.
*    Disable all lights except ``light_environment``, and set Color Profile from :guilabel:`Filmic` to :guilabel:`Standard`.

.. _tf2_v_map_method2_detailed:

Full Guide of Method 2
""""""""""""""""""""""

`SourceIO <https://github.com/REDxEYE/SourceIO>`_ will be used for :ref:`tf2_v_map_method2_detailed`. The steps to install these can be seen at the :ref:`installingprograms` section.

.. _tf2_v_importing_bsp:

Bringing the Map in
"""""""""""""""""""

.. important::

    Carefully follow these instructions. If you make a mistake, you will have to create a new, blank, project, as this addon directly reads off the ``.BSP`` in real time and doesn't allow that file to be changed or edited. There's also a lot of cleanup work to be done so, it's recommended to have a completely empty Scene for this process.

*    Go to :guilabel:`File` > :guilabel:`⤓ Import` > :guilabel:`Source Engine Assets` > :guilabel:`Source map (.bsp)` (Make sure SourceIO is installed).
*    Select your map of choice. The map **MUST** be in your TF2 game directory. It will be in ``[game_directory] / tf / maps``. You can use the name filter to narrow down the results. 

| Once loaded in, maps will be quite bare-bones. The lighting will most likely be too dark, and the props aren't there. There are a few things to set up.
*    Press A to select all objects within the viewport. Then Shift Click on an ``Empty``. 
*    An ``Empty`` is a placeholder. You'll notice a lot of these in places where Props are supposed to be.
*    Everything should be selected, with an ``Empty`` being highlighted as Orange. 
*    Hovering over the 3D Viewport, press :guilabel:`N` to open the side panel. There will be a :guilabel:`SourceIO` tab. Click on that to open it.
*    Click on :guilabel:`Load Entity`.
*    It might take some time so please be patient. If done right, all props should show up without any error messages.

| The names of the props will be a huge mess, and every single prop will end up having its own Collection. For this reason, :ref:`tf2_v_map_method1` is recommended, but otherwise, the overall Map and the Props on the map are pretty much the exact same.
| The lighting is going to appear strange because in Eevee (Blender's default render engine) has a maximum of 128 lights. Filter the Outliner (the place where all objects and things in the scene are shown) by lights with the following settings:

.. image:: _images/toggles.png
  :width: 150
  :alt: Toggles that will only show light objects. 

.. seealso::
    For a full list of Eevee's limitations, you can consult `this page <https://docs.blender.org/manual/en/latest/render/eevee/limitations.html>`_ from Blender's official manual. 

.. _tf2_v_finishing_touches:

Finishing Touches (Both Methods)
""""""""""""""""""""""""""""""""

* Use :guilabel:`Material Preview` mode to confirm that all materials are actually fully functional before you do anything else. All textures should be visible and no part of the map should be white.
* Use Eevee if you want a true TF2 look. Cycles will get you very different results.
* There's unfortunately a limit of Eevee which there's no way around. It can only have 128 active lights at once, while a lot of maps in TF2 end up having significantly more than that. Unfortunately the only way around this is to use Cycles, which doesn't have a light limit, but another alternative is to maintain the majority of the look by turning off every light except the one which starts with the name ``light_environment``. This is the 'Sun' light and is responsible for nearly all outdoor lighting and shadows present on the map.
* If you want more accurate TF2 colors, go to Color Management, and set the Color Profile from :guilabel:`Filmic` to :guilabel:`Standard`.

.. note::

    | In some maps, for example ``pl_badwater``, some universally used props will look a bit off, such as the rocks used in the starting area for the payload cart. This is because these props have multiple different skins used by different maps. A script is being developed to make it easy to change skins, but if you currently want to do it manually, then go to the Materials section of this object and make it so all the assigned faces are of a different material slot instead. If you know how Materials and Assigning works, this shouldn't be too difficult for you to do.
    | If you used SourceIO to import the map, in the sidebar (brought up by pressing the N button), there should be the option to change through different skins easily.

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

.. _tf2_v_animations:

Animations
----------

| Regardless of what method you use to import the TF2 characters and their appropriate rigs, be it the Hisanimations port, or the TF2 in game models, or the SFM models, all use the same method for applying in-game animations. There's no other method hence only one method is listed. However, for the Hisanimations port, you do have to make sure you get the one that's compatible with taunts. That one is available under the ``#community-ports`` channel of the `TF2 Blender Discord server <https://discord.gg/zHC2gJW>`_.
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
    
.. _tf2_v_weaponsandcosmetics:

Weapons and Cosmetics
---------------------

| `Hisanimations <https://youtube.com/c/hisanimations>`_ made a `video <https://youtu.be/0DMz-n1LSII>`_ explaining how to use his TF2 collection with every TF2 Weapon, Cosmetic, and Prop. Watch the video and follow the instructions.

.. _tf2_v_soundeffectsvoices:

Sound effects & Voice lines
---------------------------

| Download `GCFScape <https://nemstools.github.io/pages/GCFScape-Download.html>`_. With GCFScape, open ``tf2_sound_vo_english_dir.vpk`` for voice lines, and ``tf2_sound_misc.vpk`` for sound effects, both located in ``[game_directory] / tf``, to search for whatever you're after. You can extract it then browse it or just go through it directly in GCFScape.
