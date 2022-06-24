My projects
===========================

I don't create much new software these days, but I still find it a rewarding thing to do when I
have the time.


BrachioGraph
------------

`BrachioGraph <https://brachiograph.art>`_ is the world's simplest, cheapest drawing robot.

With a Rasberry Pi, three very cheap servo motors and some household materials, you can build a
working pen-plotter in an hour or so. It turns out to be an excellent thing to do with children on
a rainy weekend.

..  raw:: html

    <style>
        .embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; }
        .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
    </style>

    <div class='embed-container'>
    <iframe src="https://player.vimeo.com/video/372867891" allow="autoplay; fullscreen" allowfullscreen></iframe>
    </div>


C is for Camera
---------------

I've spent a lot of time repairing with old film cameras, sometimes even successfully. They contain
intricate interlocking mechanisms that implement complex sequential logic in very ingenious ways.

..  figure:: /images/canonet.jpg
    :alt:
    :class: wider

`C is for Camera <https://c-is-for-camera.readthedocs.io>`_ uses pure object-oriented Python to
simulate one of my favourite cameras, the 1972 Canon 35mm rangefinder Canonet GIII QL17.

..  code-block:: python

    >>> from camera import Camera
    >>> c = Camera()
    >>> c.film_advance_lever.wind()
    On frame 0 (of 24)
    Advancing film
    On frame 1 (of 24)
    Cocking shutter
    Applying aperture value ƒ/1.7 to iris
    Cocked
    >>> c.shutter_button.press()
    Light meter reading: ƒ1/16
    Applying aperture value ƒ/16 to iris
    Shutter opening for 1/128 seconds
    Shutter closes
    Shutter uncocked

..  figure:: /images/mechanism.jpg
    :alt:
    :class: wider
