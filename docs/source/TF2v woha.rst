.. _tf2_vanilla:

TF2 Vanilla
===========

.. contents:: Table of Contents
    :depth: 3


.. _tf2_v_mapsandprops:

Maps and included props
-----------------------

.. _map_method1:

| Method 1 uses three tools, all linked in that section. This Method is recommended as it makes the maps significantly easier to work with. All imported items are organized into collections and very easy to work with and customize.
| Method 2 uses only one addon, called SourceIO. It's a one click solution and way easier than Method 1, but the names of objects becomes a very big mess with this method, and there's extra cleanup required as extra stuff like the map hitbox is also imported. It's closer in looks to TF2 as it uses its own shader, so if you want the true TF2 look, then use this. Method 1 also works fine but is more for applying your own style or flaire to stuff.

Method 1 (Recommended)
^^^^^^^^^^^^^^^^^^^^^^

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

*    Run ``bspsrc.jar``
*    There's many options in there. Leave them be, just click the button for 'Add', and browse to your TF2 folder. From there, go to tf/maps and choose the specific .bsp (map file) you want to convert.
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

.. _Plumber:

Import .VMF files into Blender
""""""""""""""""""""""""""""""

*    In Blender, go into :guilabel:`Edit` > :guilabel:`Preferences`.
*    In the Add-ons menu, click on the :guilabel:`⤓ Install...` button.
*    Select the .ZIP file you downloaded from the `Plumber <https://github.com/lasa01/io_import_vmf/releases>`_ releases page.
*    Click on the check box to enable it.
*    It should automatically have detected any Steam products it's compatible with, such as Team Fortress 2, Left 4 Dead, Portal, Half Life 2, etc. It depends on what you have installed. Make sure you have a properly working copy of the game and it's in a valid Steam location otherwise it won't detect it.

| Plumber is now installed. You can now import a .VMF file from the :guilabel:`File` > :guilabel:`Import` > :guilabel:`Plumber` > :guilabel:`Valve Map Format (.vmf)` button. Browse to the location you stored your ``.VMF`` file which you Decompiled using BSPSource earlier, make sure that in the Import settings, the game is set to Team Fortress 2. That's it, you should have everything.
|

.. _method_2_v:

Method 2 (Alternate)
^^^^^^^^^^^^^^^^^^^^

`SourceIO <https://github.com/REDxEYE/SourceIO>`_ will be used for method 2.

.. _import_bsp_sourceio:

Import .BSP files into Blender with SourceIO
""""""""""""""""""""""""""""""""""""""""""""

.. note::

    Carefully follow these instructions. If you make a mistake, you will have to create a new, blank, project, as this addon directly reads off the ``.BSP`` in real time and doesn't allow that file to be changed or edited. This also means you should have a completely blank project before using the Add-on.

*    In Blender, go into :guilabel:`Edit` > :guilabel:`Preferences`.
*    In the Add-ons menu, click on the :guilabel:`⤓ Install...` button.
*    Select the .ZIP file you downloaded from the `SourceIO <https://github.com/REDxEYE/SourceIO>`_ releases page.
*    Click on the check box to enable it.
*    Go to :guilabel:`File` > :guilabel:`⤓ Import` > :guilabel:`Source Engine Assets` > :guilabel:`Source map (.bsp)`
*    Select your map of choice. The map **MUST** be in your TF2 game directory. It will be in ``[game_directory] / tf / maps /``. You can use the name filter to narrow down the results. 

| Once loaded in, maps will be quite bare-bones. The lighting will most likely be too dark, and the stage props aren't there. There are a few things to set up.

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
