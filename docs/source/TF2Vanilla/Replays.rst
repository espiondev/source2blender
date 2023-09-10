.. _tf2_v_replays:

Replays (demos)
===============

.. _tf2_v_autoagr:

Automatic conversion with AutoAGR
---------------------------------

This guide contains instructions for setting up and using AutoAGR. It is based on `this video by Hisanimations <https://www.youtube.com/watch?v=R_nCWv-vKg8>`_


.. _tf2_v_autoagr_setup:

Setup
^^^^^

The following add-ons are required:

*  `afx-blender-scripts <https://github.com/advancedfx/afx-blender-scripts/releases/>`_
*  `Blender Source Tools <http://steamreview.org/BlenderSourceTools/>`_
*  `The TF2 Trifecta <https://github.com/hisprofile/TF2-Trifecta/releases>`_

Software needed:

* `Team Fortress 2 <https://store.steampowered.com/app/440/Team_Fortress_2/>`_
* `HLAE <https://www.advancedfx.org/download/>`_
* `GCFScape <https://nemstools.github.io/pages/GCFScape-Download.html>`_
* `Crowbar <https://github.com/ZeqMacaw/Crowbar/releases>`_
* `Blender <https://www.blender.org/>`_

You can download AutoAGR in the :guilabel:`# announcements` channel in the `TF2 Blender Discord server <https://discord.gg/zHC2gJW>`_

.. _tf2_v_autoagr_steps:

Steps
^^^^^
Create a folder structure that ressembles this one. The GameplayModels folder's name is arbitrary.

.. code-block::

    GameplayModels/
    ├─ models/
    ├─ models2/
    │  ├─ workshop/

Open ``[game_directory] / tf / tf2_misc_dir.vpk`` with GCFScape.

Click on ``root / models`` in the left panel.

Open the ``models2`` folder in a file explorer.

From GCFScape, drag the ``weapons`` and ``player`` folders into the ``models2`` folder.

Open the ``models2 / workshop`` folder.

Double click on ``workshop`` in GCFScape.

Drag the ``weapons`` folder from GCFScape to the ``models2 / workshop`` folder.

Your folder structure should look like this once you've done all this:

.. code-block::

    GameplayModels/
    ├─ models/
    ├─ models2/
    │  ├─ player/
    │  ├─ weapons/
    │  ├─ workshop/
    │  │  ├─ weapons/

Open crowbar and click on :guilabel:`Decompile`

Enter the full path for your ``models2/`` folder under the MDL Input field. Change the :guilabel:`MDL Input` dropdown to ``Folder and subfolders``

Set the output folder to the full path for the ``models/`` folder

Under the ``Options`` Section, enable ``Folder for each model`` and click :guilabel:`decompile`

Delete ``models2/`` when the process is finished

.. danger:: Do **NOT** join a multiplayer game with HLAE or AutoAGR. This will VAC ban your Steam account.

Run AutoAGR

Set AutoAGR to this recommended configuration:

.. code-block::

    FRAMERATE: 30 / 24

    RECORD PLAYER CAMERA: YES

    RECORD OTHER PLAYERS: NO

    RECORD WEAPONS: YES

    RECORD PROJECTILES: YES

    RECORD FIRST PERSON MODELS: YES

    EXIT GAME AFTER PLAYBACK FINISHES: NO

    STARTING TICK: 1


Set the paths for the input ``.dem`` file, the ``.agr`` output file, the ``[game_directory] / tf`` folder, and the folder containing HLAE.

Click on the "write" button, then the "play" button.

Once the entire demo has been played, TF2 should go back to the home screen. Type "mirv_agr stop" and close the game.

Click on the Output properties panel and set the output frame rate to the one you chose in AutoAGR

Click on :guilabel:`File` > :guilabel:`⭳ Import` > :guilabel:`HLAE afxGameRecord (.agr)`

Set the import settings to this recommended configuration:

.. code-block::

    Asset path: folder containing the "models" folder.

    Add interpolated key frames: No

    Scale: 0.1

    Scale invisible to zero: No

    Skip Physic, LOD and Shared_Player_Skeleton meshes: Yes

    Skip Stattrack and Stickers: Yes

    Bones (skeleton) only: Yes

    Model instancing: Yes

Spawn an FK rig using the TF2 Trifecta and use Bonemerge to bind it to a rig in the scene.

If the eyes are white, select the empties in the eyes and set their Object constraint influence to 0
