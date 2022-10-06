.. _sfm:

Source Filmmaker
================

.. note::

    If you want to make sure *everything* works, be it maps, models, etc. then you'll want to make sure you have all the DLCs of SFM installed. First, launch Steam. Then go to :guilabel:`Library` and right click on Source Filmmaker. Click :guilabel:`Properties`, and go to :guilabel:`DLC`. Check the ones you need, and exit this menu. Launch SFM and create a session, it'll prompt you for the downloads. It's gonna take a while as the DLCs can go up to 7 GB in size individually, but you only have to download it once.

| Throughout these pages, you'll find clickable text where a link is provided. Just click on it or right click and 'Open in new tab' to see the contents.
| It's recommended for SFM to be installed for the best experience. You can also obtain the files using Crowbar's downloader, and most should work fine using this, but read the description of the specific map. If it says it needs other things like Prop Packs or to have DLC's, then downloading SFM is your best option.
| This entire page is written with the intent that the reader will use it for Workshop and Mods, as SFM Vanilla offers assets that are already fully available in other Source Titles, such as in Team Fortress 2. It doesn't have anything extra in Vanilla except for files present under ``tf_movies`` as Character Models, and the maps called ``stage`` and ``stage_big``. These can be obtained with the methods shown as well, just with different directories.

.. note::

    Unlike Team Fortress 2 and Garry's Mod, all the files and folders are pretty much already prepared and you don't need to do anything extra, such as turning the Add-on file into regular folders or using GCFScape to extract from ``.VPK`` files. So the steps are easier here.
    However, if using Workshop Add-ons or Mods that are specifically **maps**, the only extra step necessary is to set up Plumber. Here's how to set it up.
    
| For importing maps, Plumber won't autodetect the files from SFM like it does with other titles, so some manual work is needed. Open Blender, then go to :guilabel:`Edit` > :guilabel:`Preferences...` > :guilabel:`Add-ons`, and find Plumber. Expand it. You'll find two boxes, one on top of the other. There might be some Source Titles present in this box, such as Team Fortress 2 or Garry's Mod. If not, don't worry about it, but if it's there then it'll be helpful to view them to see how to set it up. For this box, click the ``+`` sign on the right. Label this new entry as Source Filmmaker, or as SFM. That's your choice. In the second box below, you have to manually add the directories of folders present in the Source Filmmaker folder.
| If you're confused by what that means, you're basically setting up Plumber so it pulls data from these locations and the textures all work. These will be folders with names such as ``steamapps / common / SourceFilmmaker / game / tf``, ``steamapps / common / SourceFilmmaker / game / hl2``, ``steamapps / common / SourceFilmmaker / game / tf_movies``, etc. All folders should be added. You do also have to be careful that Plumber writes the directories with ``\\`` and **NOT** with ``/``. Look at the other titles for reference if you need to. Once this is set up, Plumber should be good to go if you want to import an SFM map.
       

Contents
--------

.. toctree::
   :caption: Table of Contents
   :maxdepth: 2
   :glob:

   sfm_map
   sfm_model
   sfm_animations
   
   *
