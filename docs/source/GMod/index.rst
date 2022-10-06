.. _gmod:

Garry's Mod
===========

| Throughout this page, you'll find clickable text where a link is provided. Just click on it or right-click and 'Open in new tab' to see the contents.
| Depending on the category you'll find multiple methods or only one. Where there are multiple methods (Such as in the :ref:`gmod_map` Section), the benefits and drawbacks will be listed. Places with only one method means the other method just wasn't as good/worth it, or there only is one way to do it.
| It's best if you have an up-to-date copy of Garry's Mod installed as nearly all of these methods will be relying on obtaining files present from within the game.

.. note::
    The methods shown throughout this page are all effective on both the Vanilla files of Garry's Mod, as well as Mods and Workshop items. If using Workshop Add-ons or Mods, the only extra step necessary is to move the files in question to appropriate locations.
    A program called GMad can be used for turning ``.GMA`` files, which are used as Add-on files and are present under ``[game_directory] / garrysmod / addons``, into regular files. After that, the folders can be copied to ``[game_directory] / garrysmod``, and then the methods can be applied for bringing them in.
    If instead you obtained the files from a mod download, then you can extract those directly to ``[game_directory] / garrysmod`` without having to use GMad.
        
.. _gmod_gmad:

Turn Addons into Regular Files
------------------------------

| To turn a ``.GMA`` file into the files you need so that they can be brought into Blender, open two windows of the Game Directory, side by side. In one window, go into ``[game_directory] / garrysmod / addons``. This is where your ``.GMA`` file will be. In the other window, go to ``[game_directory] / bin``. Here, you'll find ``gmad.exe``.
| Drag and drop the ``.GMA`` file onto ``gmad.exe``. It will create a new folder with the same name as the ``.GMA`` file, in the Add-ons folder. This folder will contain everything you need for all the steps on the rest of the page.

Contents
--------

.. toctree::
   :caption: Table of Contents
   :maxdepth: 2
   :glob:

   gmod_map
   gmod_prop
   gmod_characterandrig
   gmod_animations
   gmod_weaponsandcosmetics
   gmod_soundeffectsvoices
   
   *
