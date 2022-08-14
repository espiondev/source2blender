.. _tf2_vanilla:

TF2 Vanilla
===========

| Depending on the category you'll find two methods or only one. Where there are two methods (Such as in the ``Maps and included props`` Section), the benefits and drawbacks of both will be listed. Places where there's only one method means that the other method just wasn't as good/worth it, or there only is one way to do it. The reasoning will be listed in that section.

.. contents:: Table of Contents
    :depth: 3


.. _tf2_v_mapsandprops:

Maps and included props
-----------------------

| Method 1 uses three tools, all linked in that section. This Method is recommended as it makes the maps significantly easier to work with. All imported items are organized into collections and very easy to work with and customize.
| Method 2 uses only one addon, called SourceIO. It's a one click solution and way easier than Method 1, but the names of objects becomes a very big mess with this method, and there's extra cleanup required as extra stuff like the map hitbox is also imported. It's closer in looks to TF2 as it uses its own shader, so if you want the true TF2 look, then use this. Method 1 also works fine but is more for applying your own style or flaire to stuff.
| Both methods require a fully working copy of Team Fortress 2 and a recent copy of Blender. If you are unable to get these methods to work, it is recommended to use the latest version of Blender.

.. _map_method1:

Method 1 (Recommended)
^^^^^^^^^^^^^^^^^^^^^^

.. _map_method1_summary:

Summary of Method 1
"""""""""""""""""""

| This is written here as a smaller version to come back to so you don't have to read the entire thing if you're doing the process again.
|
*    Download ``BSPSource``, ``Plumber``, and ``Blender Source Tools``. Install ``Plumber`` and ``Blender Source Tools`` into Blender. (This step is only necessary on first time use).
*    Locate map you wish to bring into Blender under ``[game_directory] / tf / maps /``.
*    Uncompress the ``.BSP`` file if necessary.
*    Convert ``.BSP`` file into ``.VMF`` file using BSPSource.
*    Import ``.VMF`` file from :guilabel:`File` > :guilabel:`Import` > :guilabel:`Plumber` > :guilabel:`Valve Map Format (.vmf)` in Blender.
*    Disable all lights except ``light_environment``, and set Color Profile from :guilabel:`Filmic` to :guilabel:`Standard`.

.. _map_method1_detailed:

Full Guide of Method 1
""""""""""""""""""""""

.. note::
    Always get the most recent version of a program or add-on linked here.

| `BSPSource <https://developer.valvesoftware.com/wiki/BSPSource>`_, `Blender Source Tools <https://developer.valvesoftware.com/wiki/Blender_Source_Tools>`_ and `Plumber <https://github.com/lasa01/io_import_vmf/releases>`_ will be used for method 1. The steps to install these will be shown later in the guide as well, you do not have to download directly from here. (Plumber was originally called io_import_vmf. This new creation is currently in Beta but significantly superior to io_import_vmf and that's why we've linked the page to download that instead.)
| BSPSource converts ``.BSP`` files (Map format used by many Source games, including TF2) to ``.VMF``. ``.VMF`` files are what will be imported into Blender using the addon called Plumber. Plumber can bring the map in, but their page says to install Blender Source Tools so specific other models, and more importantly, props on the maps, can be imported as well.

| To start off, we first need to make sure the map is usable to even import. Some maps are compressed beyond readability for BSPSource (Usually newer ones). To fix that, you need to decompile it.

.. _fix_compressed_bsp:

Fix compressed .BSP files
"""""""""""""""""""""""""

.. note::

    | These steps are only to be followed in case a .BSP file was too compressed for BSPSource.
    | However, you must follow the steps after this in the right order. 


*    Find your TF2 installation folder. You can locate it by right clicking on TF2 in your Steam library, hovering over the :guilabel:`Manage >` button, and clicking on :guilabel:`Browse local files`. This will open File Explorer in your TF2 folder. It should have a few folders in it, such as ``bin``, ``hl2``, ``platform``, ``tf``, as well as a file titled ``hl2.exe``.
*    Navigate into the ``bin`` folder.
*    Create a new .TXT file by right clicking on File Explorer, hovering over :guilabel:`New >`, and selecting :guilabel:`Text Document`. Its name doesn't matter, as long as it still has the .TXT file extension. File extensions may be hidden by default, so to enable it, click on :guilabel:`View` at the top of the window, and check the :guilabel:`File name extensions` box.
*    Open the .TXT file you just created with the text editor of your choice. Notepad should come installed on almost all Windows systems, but `Visual Studio Code <https://code.visualstudio.com/>`_ or `Notepad++ <https://notepad-plus-plus.org/>`_ can be downloaded for free online. 
*    Copy and paste the following into the .TXT file:

.. code-block:: batch
    :caption: .BSP repack script
    :linenos:

    @ECHO OFF
    SET "PScommand="POWERSHELL Add-Type -AssemblyName System.Windows.Forms; $FolderBrowse = New-Object System.Windows.Forms.OpenFileDialog -Property @{ValidateNames = $false;CheckFileExists = $false;RestoreDirectory = $true;FileName = 'Selected Folder';};$null = $FolderBrowse.ShowDialog();$FolderName = Split-Path -Path $FolderBrowse.FileName;Write-Output $FolderName""
    FOR /F "usebackq tokens=*" %%Q in (`%PScommand%`) DO (
        SET FOLDER=%%Q
    )
    echo FOLDER
    bspzip -repack FOLDER
    PAUSE
    EXIT

*    Save and close out of the text editor.

.. warning::

   **Save a backup of this map you are about to repack, as this script may overwrite the original file.**

*    Rename the file to have a .BAT extension. You will be warned that the file may become unusable. Click :guilabel:`Yes`.
*    Double click on the batch script for it to run. It will prompt you with a destination folder to choose.

| The repacked .BSP file is now in the selected folder. You can use BSPSource to convert it to a .VMF now. 
|

.. _convert_bsp_to_vmf:

Convert a .BSP to .VMF
""""""""""""""""""""""

.. important::

    You need to install `Java <https://www.java.com/download/ie_manual.jsp>`_ to run BSPSource.

*    Download `BSPSource <https://developer.valvesoftware.com/wiki/BSPSource>`_ and extract it.
*    Run ``bspsrc.jar``
*    There's many options in the program. Leave them be, just click the button for 'Add', and browse to your TF2 folder. From there, go to ``tf / maps`` and choose the specific ``.BSP`` (map file) you want to convert.
*    Once that's done, just click the Decompile button in the bottom right, there's no need to edit the other settings, though you're free to play around if you personally want to.
*    A file browser will show up for where to put the ``.VMF`` file. You can choose any location, but it's best if it's a place you can easily come back to.
*    Click on :guilabel:`Decompile`.

| Your .VMF file has now been decompiled and is in your output folder.
|

.. _install_bst:

Install Blender Source Tools
""""""""""""""""""""""""""""

*    In Blender, go into :guilabel:`Edit` > :guilabel:`Preferences`.
*    In the Add-ons menu, click on the :guilabel:`⤓ Install...` button.
*    Select the .ZIP file you downloaded from the `Blender Source Tools <https://developer.valvesoftware.com/wiki/Blender_Source_Tools>`_ website.
*    Click on the check box to enable it.

| Blender Source Tools is now installed. You'll notice its settings show up under the :guilabel:`⤓ Import` section in the :guilabel:`File` menu on the top left of Blender.
|

.. _install_Plumber:

Import .VMF files into Blender
""""""""""""""""""""""""""""""

*    In Blender, go into :guilabel:`Edit` > :guilabel:`Preferences`.
*    In the Add-ons menu, click on the :guilabel:`⤓ Install...` button.
*    Select the .ZIP file you downloaded from the `Plumber <https://github.com/lasa01/io_import_vmf/releases>`_ releases page.
*    Click on the check box to enable it.
*    It should automatically have detected any Steam products it's compatible with, such as Team Fortress 2, Left 4 Dead, Portal, Half Life 2, etc. It depends on what you have installed. Make sure you have a properly working copy of Team Fortress 2 and it's in a valid Steam location otherwise it won't detect it.

| Plumber is now installed. 
| 
| You can now import a .VMF file from the :guilabel:`File` > :guilabel:`Import` > :guilabel:`Plumber` > :guilabel:`Valve Map Format (.vmf)` button. Browse to the location you stored your ``.VMF`` file which you Decompiled using BSPSource earlier, make sure that in the Import settings, the game is set to Team Fortress 2. That's it, you should have everything. If you wish to repeat this whole process for another map, a Summary is written at the top of the Method 1 section which you can refer to.
|

.. _map_method2:

Method 2 (Alternate)
^^^^^^^^^^^^^^^^^^^^

.. _map_method2_summary:

Summary of Method 2
"""""""""""""""""""

| This is written here as a smaller version to come back to so you don't have to read the entire thing if you're doing the process again.
|
*    Download SourceIO and install it into Blender.
*    Import ``.BSP`` file from :guilabel:`File` > :guilabel:`Import` > :guilabel:`Source Engine Assets` > :guilabel:`Source Map (.bsp)` in Blender.
*    Locate map you wish to bring into Blender under ``[game_directory] / tf / maps /``
*    Select everything by pressing A, Shift Click an ``Empty``
*    Press N under Viewport to open a side menu, go to SourceIO in that menu, and click ``Load Entity``
*    Disable all lights except ``light_environment``, and set Color Profile from :guilabel:`Filmic` to :guilabel:`Standard`.

.. _map_method2_detailed:

Full Guide of Method 2
""""""""""""""""""""""

`SourceIO <https://github.com/REDxEYE/SourceIO>`_ will be used for method 2.

.. _import_bsp_sourceio:

Installing and using SourceIO
"""""""""""""""""""""""""""""

.. note::

    Carefully follow these instructions. If you make a mistake, you will have to create a new, blank, project, as this addon directly reads off the ``.BSP`` in real time and doesn't allow that file to be changed or edited. This also means you should have a completely blank project before using the Add-on.

*    In Blender, go into :guilabel:`Edit` > :guilabel:`Preferences`.
*    In the Add-ons menu, click on the :guilabel:`⤓ Install...` button.
*    Select the .ZIP file you downloaded from the `SourceIO <https://github.com/REDxEYE/SourceIO>`_ releases page.
*    Click on the check box to enable it.
*    Go to :guilabel:`File` > :guilabel:`⤓ Import` > :guilabel:`Source Engine Assets` > :guilabel:`Source map (.bsp)`
*    Select your map of choice. The map **MUST** be in your TF2 game directory. It will be in ``[game_directory] / tf / maps /``. You can use the name filter to narrow down the results. 

| Once loaded in, maps will be quite bare-bones. The lighting will most likely be too dark, and the props aren't there. There are a few things to set up.

*    Press A to select all objects within the viewport. Then Shift Click on an ``Empty``. An ``Empty`` is a placeholder. You'll notice a lot of these in places where Props are supposed to be.
*    Hovering over the 3D Viewport, press :guilabel:`N` to open the side panel. There will be a :guilabel:`SourceIO` tab. Click on that to open it.
*    Click on :guilabel:`Load Entity`.
*    It might take some time so please be patient. If done right, all props should show up without any error messages, and there will also now be a lot of Collections.

| The lighting is going to appear strange because in Eevee (Blender's default render engine) has a maximum of 128 lights. Filter the Outliner by lights with the following settings

.. image:: _images/toggles.png
  :width: 150
  :alt: Toggles that will only show light objects. 

.. _MapPrep:

Finishing Touches
"""""""""""""""""

* Go to :guilabel:`Material Preview` mode to confirm that all materials are actually fully functional before you do anything else.
* Use Eevee if you want a true TF2 look. Cycles will get you very different results.
* There's unfortunately a limit of Eevee which there's no way around. It can only have 128 active lights at once, while a lot of maps in TF2 end up having significantly more than that. Unfortunately the only way around this is to use Cycles, which doesn't have a light limit, but another alternative is to maintain the majority of the look by turning off every light except the one which starts with the name ``light_environment``. This is the 'Sun' light and is responsible for nearly all outdoor shadows present on the map.
* If you want more accurate TF2 colors, go to Color Management, and set the Color Profile from :guilabel:`Filmic` to :guilabel:`Standard`.

.. note::

    | In some maps, for example ``pl_badwater``, some universally used props will look a bit off, such as the rocks used in the starting area for the Payload Cart. This is because these props have multiple different skins used by different maps. A script is being developed to make it easy to change skins, but if you currently want to do it manually, then go to the Materials section of this object and make it so all the assigned faces are of a different material slot instead. If you know how Materials and Assigning works, this shouldn't be too difficult for you to do.
    | If you used SourceIO to bring the map in, then in the N menu there should be the option to change through different skins easily.
| 

.. _tf2_v_individualprops:

Individual Props
----------------

| This section is written as a way to obtain individual props universally used in maps stored in the TF2 files, such as Barrels or Control Points or Gates. Some maps will have props that aren't used universally, and are exclusive to them. In this case it's best to just import the map, find the prop, and separate it.
| Although this part is possible to do with both Plumber and BSPSource, it's so much more of a hassle that we didn't even think it was worth writing the Plumber method. If for any reason you're still interested in that method, you can contact us on Discord and we can tell you about it.
| 

.. _prop_method1:

Method
^^^^^^

| The process is rather simple, just needs a bit of setup then the importing of the prop should be doable with one click.
|
*    Download `GCFScape <https://nemstools.github.io/pages/GCFScape-Download.html>`_, and `SourceIO <https://github.com/REDxEYE/SourceIO>`_.
*    In Blender, go into :guilabel:`Edit` > :guilabel:`Preferences`.
*    In the Add-ons menu, click on the :guilabel:`⤓ Install...` button.
*    Select the .ZIP file you downloaded from the `SourceIO <https://github.com/REDxEYE/SourceIO>`_ releases page.
*    Click on the check box to enable it.
*    Go to ``[game_directory] / tf`` and open the file called ``tf2_misc_dir.vpk``. It should open through GCFScape.
*    Drag the window of the ``[game_directory] / tf`` folder so that it's visible, as you can drag and drop files.
*    Drag the ``Models`` folder into ``[game_directory] / tf``.
*    Go to the ``Materials`` folder. Inside of it there should be another folder called ``Models``. Drag this to ``[game_directory] / tf`` as well.
*    Once extracted, you may close GCFScape and open another file called ``tf2_textures_dir.vpk``. There should be another folder inside called ``Models``. Drag this to ``[game_directory] / tf``.
|
| All of that was for setting things up. Once that's completed, all you have to do for bringing a Model in is to open Blender, click :guilabel:`File` > :guilabel:`⤓ Import` > :guilabel:`Source Engine Assets` > :guilabel:`Source model (.mdl)`, and choose the ``.MDL`` file you're after inside the ``Models`` folder. It should have textures set up and everything.

.. _tf2_v_characterandrig:

Character and Rig
-----------------

| Method 1 is easier to do as, the work is already done. `Hisanimations <https://youtu.be/7rH6_eq-I0c>`_ from the `TF2 Blender Discord Server <https://discord.gg/zHC2gJW>`_ has already made a fully working Character Ports file that you can use for yourself. Click on his name and it'll take you to a YouTube video where he explains what it is and how to use it. That's literally it we don't even have to write more about it here. If you have any questions about it then join the Discord server and you can ask there. This one is recommended in most cases, but if you're going to do Animation work, and especially long animation work, then Method 2 is recommended, as it gives significantly better performance.
| Method 2 is to extract all the Characters and Rigs from the actual game. Three tools are used. It's definitely not as simple of a method, as in Method 1 everything is already done for you. You should only do this if you'll be doing animations and need the max performance.
| Method 2 requires a fully working copy of Team Fortress 2 and a recent copy of Blender. You don't need a copy of the game to use Method 1. If you are unable to get these methods to work, it is recommended to use the latest version of Blender.

.. _characterandrig_method1:

Method 1 (Recommended)
^^^^^^^^^^^^^^^^^^^^^^

| Go to `This Youtube Video <https://youtu.be/7rH6_eq-I0c>`_ and follow the instructions.

.. _characterandrig_method2:

Method 2 (Alternate)
^^^^^^^^^^^^^^^^^^^^

.. _characterandrig_method2_summary:

Summary of Method 2
"""""""""""""""""""

| This is written here as a smaller version to come back to so you don't have to read the entire thing if you're doing the process again.
|
*    Download ``GCFScape``, ``Blender Source Tools``, and ``Crowbar``. Install ``Blender Source Tools`` as an addon into Blender. (This step is only necessary for first time use).
*    Extract the necessary class files into a folder of your choice.
*    Open the ``.MDL`` file in Crowbar and Decompile it into another folder.
*    Use Blender Source Tools to import the ``.QC`` file
*    Remove or hide any unnecessary objects such as the Hitbox or extra LODs.

.. _characterandrig_method2_detailed:

Full Guide of Method 2
""""""""""""""""""""""

.. note::

    | If you want better quality models, you'll have to adventure to the lands of SFM. Within that are files under a directory called ``tf_movies``. The Character Models under this directory are much higher quality than the ones which can be found within TF2's own files, and if you have SFM installed or know someone who has it installed, it's **HIGHLY** recommended to use these instead. You don't lose out on much, if any performance if using these. If you're going this route, you'll know you did it right when the Crowbar decompiled files have SFM in their names.
|

*    Download `GCFScape <https://nemstools.github.io/pages/GCFScape-Download.html>`_, `Crowbar <https://steamcommunity.com/groups/CrowbarTool>`_, and `Blender Source Tools <https://developer.valvesoftware.com/wiki/Blender_Source_Tools>`_.
*    Go to ``[game_directory] / tf`` and open the file called ``tf2_misc_dir.vpk``. It should open through GCFScape.
*    Go to ``models / player / hwm``. You'll find a bunch of files with the class names. These are models used in game. If you're using the SFM files, only the specific directories differ but the process is the same, so continue reading.
*    Extract all files with the same name (For example, if you want to import Heavy, then extract all files starting with the name ``heavy_``) to a new folder.
*    Open Crowbar, and go to the :guilabel:`Decompile` tab. For the ``MDL`` file, select the ``.MDL`` from the files you just extracted through GCFScape.
*    For the Output Folder, make a new folder or choose an existing one to Decompile to.
*    You don't need to change any settings, but do make sure that the checkbox :guilabel:`QC File` is enabled.
*    Click :guilabel:`Decompile` in the bottom left.
*    In Blender, go into :guilabel:`Edit` > :guilabel:`Preferences`.
*    In the Add-ons menu, click on the :guilabel:`⤓ Install...` button.
*    Select the .ZIP file you downloaded from the `Blender Source Tools <https://developer.valvesoftware.com/wiki/Blender_Source_Tools>`_ page.
*    Click on the check box to enable it.
*    Finally, In Blender, go into :guilabel:`File` > :guilabel:`Import` > :guilabel:`Source Engine (.smd, .vta, .dmx, .qc)`.
*    Go to the folder where ``Crowbar`` Decompiled the files. In there you should find multiple files, click on the one that ends with ``.QC``.
*    If everything was done right, you should now have the model in Blender with a fully working rig.

| Some cleanup would be required, as there's extra objects and meshes you don't really need, like LODs or a Vertex Cloud or the Hitbox. The highest quality Object is the one which doesn't have LOD in the name. It's parented to ``(class).qc_skeleton``. The rig is fully working, extra weight paint or work isn't needed.

.. note::

    | If you used TF2's in-game files, then inside GCFScape when you're extracting the files, you might have noticed that similar files were also under ``models / player``. The difference between these files and the ones inside ``models / player / hwm`` is only of the mouth supposedly having HWM properties. HWM, or **H**ard**W**are **M**orph System, is used by VALVe for facial reflexes and stuff. But according to Hisanimations, the files are there but the game doesn't use them. Whether you use files under ``models / player`` or ``models / player / hwm``, doesn't matter. Other than the mouth, both have the exact same mesh and their quality will be the same.

.. _tf2_v_animations:

Animations
----------

| Regardless of what method you use to bring in the TF2 Characters and their appropriate Rigs, be it the Hisanimations port, or the TF2 in game models, or the SFM models, all use the same Method for applying in-game Animations. There's no other method hence only one Method is listed. However, for the Hisanimations port, you do have to make sure you get the one that's compatible with Taunts. That one is available under the #community-ports channel of the TF2-Blender discord server.
| 

.. note::

    | Not all animations from TF2 can be brought in with ease. Some can, but not all. It depends on which specific animation you want to bring in. Some animations in TF2 are additive, instead of independent, meaning that you need a base animation and the new animation adds on top of it. For example, to bring in the animation of shooting the shotgun, you first need to have the idle animation of that shotgun brought in.
    | This is possible in SFM however for Blender, a script is required. It's currently being worked on by Hisanimations and not completed at the time of writing.

.. _animations_method1:

Method
^^^^^^

*    Download `GCFScape <https://nemstools.github.io/pages/GCFScape-Download.html>`_, `Crowbar <https://steamcommunity.com/groups/CrowbarTool>`_, and `Blender Source Tools <https://developer.valvesoftware.com/wiki/Blender_Source_Tools>`_.
*    Go to ``[game_directory] / tf`` and open the file called ``tf2_misc_dir.vpk``. It should open through GCFScape.
*    Drag the window of the ``[game_directory] / tf`` folder so that it's visible, as you can drag and drop files.
*    Extract the ``models`` folder to ``[game_directory] / tf`` 
*    Go to ``models / player`` and find ``(class)_animations.mdl``. Copy it to another location, preferably a new folder. This is the file that holds almost all animation data for that specific class.
*    Repeat the process for ``models / workshop / player / animations``. Just in case the specific animation can't be found in that first ``.MDL`` file, we'll get the remaining ones from here too.
*    Open Crowbar, and go to the :guilabel:`Decompile` tab. For the ``MDL`` file, select the ``.MDL`` from the files you just extracted through GCFScape.
*    For the Output Folder, make a new folder or choose an existing one to Decompile to.
*    You don't need to change any settings, click :guilabel:`Decompile` in the bottom left. If done right, the folder should have a very large amount of ``.SMD`` files.
*    In Blender, go into :guilabel:`Edit` > :guilabel:`Preferences`.
*    In the Add-ons menu, click on the :guilabel:`⤓ Install...` button.
*    Select the .ZIP file you downloaded from the `Blender Source Tools <https://developer.valvesoftware.com/wiki/Blender_Source_Tools>`_ page.
*    Click on the check box to enable it.
*    Finally, In Blender, click on the specific skeleton you want to apply an animation to (You do have to import the Character first. You can't just bring the animation into an empty scene.)
*    Go into :guilabel:`File` > :guilabel:`Import` > :guilabel:`Source Engine (.smd, .vta, .dmx, .qc)`.
*    Go to the folder where ``Crowbar`` Decompiled the files. In there you should find multiple files, all with a lot of names. Find the one that you're after, and import it.
*    If everything was done right, the Timeline in Blender should adjust itself and by pressing Spacebar, the Animation should be visible.

.. note::

    | As of writing this, in some cases you can find two identically named files, one name starting with taunt_ and the other name starting with layer_taunt_. These are different files. As of writing, it is uncertain which is the one to use but, if one file doesn't give the wanted results, try the other. Also, not every animation is guaranteed to work, even if it's not an Additive taunt.
    | All animations are designed to be played back at 30fps. If you know how to animate then changing the framerate of this shouldn't be difficult.
