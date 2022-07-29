TF2 (Vanilla)
=============

.. contents:: Table of Contents
    :depth: 2


Maps and included props
-----------------------

Method 1 (Recommended)
^^^^^^^^^^^^^^^^^^^^^^

| `BSPSource <https://developer.valvesoftware.com/wiki/BSPSource>`_, `Blender Source Tools <https://developer.valvesoftware.com/wiki/Blender_Source_Tools>`_ and `io_import_vmf <https://github.com/lasa01/io_import_vmf>`_ will be used for method 1.
| BSPSource converts *.BSP*   files (Map format used by some Source games) to *.VMF*. *.VMF*   files are what will be imported into Blender. 
| Some maps are compressed beyond readability for BSPSource (Usually newer ones). To fix that, you need to repack it with a batch script file.

How to fix compressed .BSP files
""""""""""""""""""""""""""""""""

.. note::

    | These steps are only to be followed in case a .BSP file was too compressed for BSPSource.
    | However, you must follow the steps after this in the right order. 


*    Find your TF2 installation folder. You can locate it by right clicking on TF2 in your Steam library, hovering over the :guilabel:`Manage >` button, and clicking on :guilabel:`Browse local files`.
This will open File Explorer in your TF2 folder. It should have a few folders in it, such as "bin", "hl2", "platform", "tf", as well as a file titled hl2.exe".
*    Navigate into the "bin" folder.
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

How to convert a .BSP to .VMF
"""""""""""""""""""""""""""""

*    Run "bspsrc.jar"
*    Because of the outdated (as of writing) file selection dialog, it is recommended to simply drag and drop your .BSP file.
*    You will be prompted to choose an output folder. Choose one that isn't too cluttered so it isn't too hard locating your file.
*    Click on :guilabel:`Decompile`.
| Your .VMF file has been decompiled and is in your output folder.
| 

How to install Blender Source Tools
"""""""""""""""""""""""""""""""""""

*    In Blender, go into :guilabel:`Edit` > :guilabel:`Preferences`.
*    In the Add-ons menu, click on the :guilabel:`⤓ Install...` button.
*    Select the .ZIP file you downloaded from the Blender Source Tools website.
*    Click on the check box to enable it.
| Blender Source Tools is now installed.
|

How to import .VMF files into Blender
"""""""""""""""""""""""""""""""""""""

.. note::

    io_import_vmf requires Blender Source Tools to be installed. if you followed the last steps, you should be fine.

*    Follow the same steps to install io_import_vmf as you installed Blender Source Tools.
*    Click on the arrow to the left of it to open the settings.
*    Choose a cache directory path. This should be its own empty folder.
*    Click the :guilabel:`+` button under the "Valve game definitions: " section.
*    Click on :guilabel:`Detect from a game directory`.
*    Navigate to your TF2 game installation folder. Select the "tf" folder.
| io_import_vmf is now installed. You can now import a .VMF file from the :guilabel:`File` > :guilabel:`Import` > :guilabel:`Valve Map Format (.vmf)` button. Importing most maps will likely freeze Blender, but wait for it to finish.
|