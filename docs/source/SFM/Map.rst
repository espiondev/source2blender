.. _sfm_map:

Maps and included props
-----------------------

| This :ref:`sfm_map_method1` uses three tools, all linked in that section.
| Unlike Team Fortress 2 and GMod, SFM maps are a bit complicated and pull resources from multiple different folders. SourceIO has not been successful for the importing of maps, but has been fine for everything else. For this reason, the Map Import section only has one method.
| This method requires a fully working copy of Source Filmmaker and a recent version of Blender. If you are unable to get this method to work, it is recommended to use the latest version of Blender.
|
| Also make sure to follow the note under :ref:`sfm` for how to set up Plumber so it actually reads SFM files.

.. _sfm_map_method1:

Method
^^^^^^

.. _sfm_map_method1_summary:

Summary of Method
"""""""""""""""""

*    Download BSPSource, Plumber, and Blender Source Tools. Install Plumber and Blender Source Tools as Add-ons into Blender (This step is only necessary on first time use).
*    Set up an entry in Plumber for it to read all of SFM's folders present under ``[sfm_directory] / game`` (This step is only necessary on first time use).
*    Locate the map you wish to bring into Blender by going to ``[sfm_directory] / game / workshop / maps``.
*    Convert the ``.BSP`` file into a ``.VMF`` file using BSPSource.
*    Import the ``.VMF`` file from :guilabel:`File` > :guilabel:`Import` > :guilabel:`Plumber` > :guilabel:`Valve Map Format (.vmf)` in Blender.
*    Disable all lights except ``light_environment``, and set Color Profile from :guilabel:`Filmic` to :guilabel:`Standard`.

.. _sfm_map_method1_detailed:

Full Guide of Method
""""""""""""""""""""

.. note::
    Always get the most recent version of a program or Add-on linked here.

| `Blender Source Tools <http://steamreview.org/BlenderSourceTools>`_, `BSPSource <https://developer.valvesoftware.com/wiki/BSPSource>`_, and `Plumber <https://github.com/lasa01/io_import_vmf/releases>`_ will be used for this method. The steps to install these can be seen at the :ref:`installingprograms` section. 
| Plumber was originally called io_import_vmf, and it's by the same developers. It's currently in Beta but significantly superior to io_import_vmf and that's why we've linked the page to download that instead.

.. _sfm_convert_bsp_to_vmf:

Convert a .BSP to .VMF
""""""""""""""""""""""

.. important::

    You need to install `Java <https://www.java.com/download/ie_manual.jsp>`_ to run BSPSource.

*    Download `BSPSource <https://developer.valvesoftware.com/wiki/BSPSource>`_ and extract all files to a folder.
*    Open ``bspsrc.jar`` from this folder.
*    There's many options in the program. For now, just click the button for :guilabel:`Add`. From there, go to ``[SFM_directory] / game / workshop / maps`` and choose the specific ``.BSP`` map file you want to convert.
*    Go to the :guilabel:`Other` tab in BSPSource, and enable the checkbox labelled :guilabel:`Extract Embedded Files`.
*    Once done, just click the :guilabel:`Decompile` button in the bottom right. There's no need to edit the other settings, though you're free to play around if you know what you're doing.
*    A file browser will show up for where to put the ``.VMF`` file. You can choose any location, but it's best if it's a place you can easily come back to.
*    Click on :guilabel:`Decompile`.

| Your .VMF file has now been decompiled and is in your output folder. You'll notice another folder in that location with the same name as the ``.VMF`` file. We'll use this later. If such a folder doesn't exist, then don't worry about it.

.. important::

    During the time that BSPSource is Decompiling the map, it will show logs of what it's doing. There is an ``Errors & Warnings`` box visible. If the process worked, then this box should be mostly empty. If [Warning] is shown in this, then it should be fine. If an [Error] is shown in this, however, then it may have failed. You'll have to come back to this step if the map doesn't work later. 

.. _sfm_importing_vmf:

Bringing The Map In
"""""""""""""""""""

| You can now import a .VMF file from the :guilabel:`File` > :guilabel:`Import` > :guilabel:`Plumber` > :guilabel:`Valve Map Format (.vmf)` button (Make sure Plumber and Blender Source Tools are installed). Browse to the location you stored your ``.VMF`` file which you Decompiled using BSPSource earlier. 
*    Make sure that in the Import settings, the game is set to Team Fortress 2. 
*    Set the Scale to 0.1, and the Light Brightness set to 10. This is so the map is compatible with the Hisanimations Characters port and TF2 Collections Port.
*    In the folder space underneath the :guilabel:`Game`, type the name of the folder with the same name as the ``.VMF``. So if for example, your map file is called ``fnaf1_sfm_d.vmf`` then there should also be a folder called ``fnaf1_sfm_d``. Write ``fnaf1_sfm_d`` in that space. If you don't have such a folder, you can skip this step.
*    Then click the ``.VMF`` file, and click :guilabel:`Import`. That's it, you should have everything. 

| The installation steps are not necessary to do again. It's really just as simple as, Once you set up Plumber so it reads the SFM folders, all you have to do is turn the ``.BSP`` map file into ``.VMF`` with BSPSource, and bring ``.VMF`` into Blender with Plumber.
| Go to :ref:`sfm_finishing_touches` for advice on clean up and additional useful things to know about within Blender regarding these maps.
| If you wish to familiarize yourself with the whole process, or see an overview, a :ref:`sfm_map_method1_summary` is written which you can refer to.
| If any problems occur you can ask for help on the `TF2 Blender Discord server <https://discord.gg/zHC2gJW>`_.

| The lighting is going to appear strange because in Eevee (Blender's default render engine) has a maximum of 128 lights. Filter the Outliner (the place where all objects and things in the scene are shown) by lights with the following settings:

.. image:: _images/toggles.png
  :width: 150
  :alt: Toggles that will only show light objects. 

.. seealso::
    For a full list of Eevee's limitations, you can consult `this page <https://docs.blender.org/manual/en/latest/render/eevee/limitations.html>`_ from Blender's official manual. 

.. _sfm_finishing_touches:

Finishing Touches
"""""""""""""""""

* Use :guilabel:`Material Preview` mode to confirm that all materials are actually fully functional before you do anything else. All textures should be visible and no part of the map should be white.
* Use Eevee if you want a true Source look. Cycles will get you very different results.
* There's unfortunately a limit of Eevee which there's no way around. It can only have 128 active lights at once, while a lot of maps can have more than that. Unfortunately the only way around this is to use Cycles, which doesn't have a light limit, but another alternative is to maintain the majority of the look by turning off every light except the one which starts with the name ``light_environment``. This is the 'Sun' light and is responsible for nearly all outdoor lighting and shadows present on the map.
* If you want more accurate Source colors, go to Color Management, and set the Color Profile from :guilabel:`Filmic` to :guilabel:`Standard`.
