.. _tf2_vanilla:

TF2-Vanilla
===========

.. contents:: Table of Contents
    :depth: 3


.. _maps_and_props_v:

Maps and included props
-----------------------

.. _method_1_v:

Method 1 (Recommended)
^^^^^^^^^^^^^^^^^^^^^^

.. note::
    Always get the most recent version of a program or add-on linked here.

| `BSPSource <https://developer.valvesoftware.com/wiki/BSPSource>`_, `Blender Source Tools <https://developer.valvesoftware.com/wiki/Blender_Source_Tools>`_ and `io_import_vmf / Plumber <https://github.com/lasa01/io_import_vmf/releases>`_ will be used for method 1.
| BSPSource converts ``.BSP`` files (Map format used by some Source games) to .VMF. .VMF files are what will be imported into Blender. 
| Some maps are compressed beyond readability for BSPSource (Usually newer ones). To fix that, you need to repack it with a batch script file.

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
    |

*    Rename the file to have a .BAT extension. You will be warned that the file may become unusable. Click :guilabel:`Yes`.
*    Double click on the batch script for it to run. It will prompt you with a destination folder to choose.

| The repacked .BSP file is now in the selected folder. You can use BSPSource to convert it to a .VMF now. 
|

.. _convert_bsp_to_vmf:

Convert a .BSP to .VMF
""""""""""""""""""""""

.. important:: DEPENDANCIES

    You need to install `Java <https://www.java.com/download/ie_manual.jsp>`_ to run BSPSource.


*    Run ``bspsrc.jar``
*    Because of the outdated (as of writing) file selection dialog, it is recommended to simply drag and drop your .BSP file.
*    You will be prompted to choose an output folder. Choose one that isn't too cluttered so it isn't difficult to locate your file.
*    Click on :guilabel:`Decompile`.

| Your .VMF file has been decompiled and is in your output folder.
|

.. _install_bst:

Install Blender Source Tools
""""""""""""""""""""""""""""

*    In Blender, go into :guilabel:`Edit` > :guilabel:`Preferences`.
*    In the Add-ons menu, click on the :guilabel:`⤓ Install...` button.
*    Select the .ZIP file you downloaded from the Blender Source Tools website.
*    Click on the check box to enable it.

| Blender Source Tools is now installed.
|

.. _import_vmf:

Import .VMF files into Blender
"""""""""""""""""""""""""""""""""""""

.. note::

    | io_import_vmf, which has recently been renamed to Plumber, requires Blender Source Tools to be installed. if you followed the steps to install it, you should be fine.
    | If you downloaded the most recent version of the add-on, you don't need to follow these steps. It's been automated.


*    Follow the same steps to install io_import_vmf as you installed Blender Source Tools.
*    Click on the arrow to the left of it to open the settings.
*    Choose a cache directory path. This should be its own empty folder.
*    Click the :guilabel:`+` button under the "Valve game definitions: " section.
*    Click on :guilabel:`Detect from a game directory`.
*    Navigate to your TF2 game installation folder. Select the "tf" folder.

| io_import_vmf is now installed. You can now import a .VMF file from the :guilabel:`File` > :guilabel:`Import` > :guilabel:`Valve Map Format (.vmf)` button. Importing most maps will likely freeze Blender, but wait for it to finish.
|

.. _method_2_v:

Method 2 (Alternate)
^^^^^^^^^^^^^^^^^^^^

`SourceIO <https://github.com/REDxEYE/SourceIO>`_ will be used for method 2.

.. _import_bsp_sourceio:

Import .BSP files into Blender with SourceIO
""""""""""""""""""""""""""""""""""""""""""""

.. note::

    Carefully follow these instructions. If you make a mistake, you will have to delete everything (hundreds of objects) from the current scene and try again, or create a new, blank, project instead (which is easier).

*    Follow the steps in ":ref:`install_bst`" to install SourceIO. No setup necessary.
*    Go to :guilabel:`File` > :guilabel:`⤓ Import` > :guilabel:`Source Engine Assets` > :guilabel:`Source map (.bsp)`
*    Select your map of choice. The map **MUST** be in your TF2 game directory. It will be in ``[game_directory] / tf / maps /``. You can use the name filter to narrow down the results. 

| Once loaded in, maps will be quite bare-bones. Lhe lighting will most likely be too dark, and the stage props aren't there. There are a few things to set up.

*    In the Outliner (panel on the right that lists all objects in the scene), scroll down until you see a collection of props represented by objects known as "empty". You can also move your mouse to the right and drag the scroll bar down, which is faster.
Default Blender icon for an empty.
.. image:: _images/empty.png
  :width: 150
  :alt: The default Blender icon for an empty

*    Left click to select the top-most empty. If you ever accidentally select another one, select the top one again.
*    Scroll down until you see the last empty prop. :guilabel:`Shift` + click on it to select all objects between the top and bottom one.
*    Hovering over the 3D Viewport, press :guilabel:`N` to open the side panel. There will be a :guilabel:`SourceIO` tab.
*    Click on :guilabel:`Load Entity`.

| You have loaded the map's props. Repeat this if there are any more Collections of props you need visible.
| The lighting is going to appear strange because in Eevee (Blender's default render engine) has a maximum of 128 lights. Filter the Outliner by lights with the following settings

.. image:: _images/toggles.png
  :width: 150
  :alt: Toggles that will only show light objects. 

.. seealso::

    `Full list of Eevee's limitations <https://docs.blender.org/manual/en/dev/render/eevee/limitations.html>`_
    |

| In some cases, you can delete every light except for the one called ``light_environment`` (the sun light), which will be in the ``light_environment`` collection. You can also go into edit mode and delete the outer faces of the skybox. You can replace them with any of the hundreds of free, high-resolution HDRI textures from `Poly Haven <https://polyhaven.com/hdris>`_
| Otherwise, you may want to manually delete each light individually if it doesn't add to the scene's lighting.

