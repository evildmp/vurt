.. _on-teaching:

========================
On teaching
========================

*1st June 2025*

-----------

An idea that has informed how I think about learning (and what I do when I want someone to learn something) is that *I can't teach; all I can do is provide a learning experience*.

I think it must be one of the most important things I believe.

It's a foundational concept in `Diátaxis <https://diataxis.fr/tutorials/>`_.

I use it all the time in training and documentation, and spend a lot of time urging other people to let themselves be guided by it.

Almost daily, when I remember to put it into practice it makes a difference to things I do with other people, and rewards me for it.

---------

In 2005 I was a high-school teacher, teaching ICT - Information and Communications Technology. It was an unattractive name for an unsatisfactory subject, and I quickly realised I didn't enjoy it.

The curriculum (`EdExcel's Intermediate GNVQ Information and Communications Technology <https://web.archive.org/web/20051206020755/http://www.edexcel.org.uk/quals/gnvq/ict/int/gy206/>`_) had no feeling for computers or computing. It didn't connect with the ideas and open-ended possibilities of computing that make it exciting, nor with the rigour and precision that give it meaning.

I was also unimpressed with the way it was delivered at the school. I thought it was unimaginative and sloppy.


"Word is the best way to do it!"
================================

At one point, I was assigned to teach a several-week-long module, in which the 16-year-olds were going to make websites.

I recoiled with real horror from the teaching materials I'd been given.


Their version
-------------

..  sidebar::

    For a taste of how the official curriculum treated the topic, see pages 56-57 of the `GNVQ specification <https://web.archive.org/web/20051214163525/http://www.edexcel.org.uk/VirtualContent/70345.pdf>`_, sections *Computer programming* and *Html programs [sic]*.

The handouts for the pupils instructed them to create web pages using Microsoft Word, of all things (not even FrontPage, which was part of the same MS Office suite installed on all the school's computers).

"Word is the best way to do it!" I was told, when I questioned this.

The coursework would have had the pupils "designing their web pages" in Word - writing text, adding links ("hot spots", according to the curriculum), images, clip art and animation and formatting ("to make it interesting") and then saving their work as web pages. It was perfectly horrible.

My version
----------

Over that weekend I wrote the materials for a completely new version of the module. It began with with creating the most minimal HTML page in a plain text editor, and moved on to include all the things covered by the curriculum (images, links, styling, navigation menus and so on). I emphasised correctness (using the W3C validator, styling in a CSS style sheet, alt text - the usual basic practices that we take for granted).

On Monday I made a real nuisance of myself, and after he had had enough of my argument and pleading the head of department begrudgingly conceded that what I had prepared did indeed seem to meet the requirements of the curriculum. He agreed that I could deliver my version of the module.


In the classroom
================

There was some bewilderment on the part of the pupils, and even some resistance. Many aspects of what they were being asked to do were completely unfamiliar. In several years of ICT lessons they had barely been required to use any software that wasn't part of MS Office.

One of the biggest challenges for them to get over was the idea that *what they were doing* looked nothing like *what was produced as a result*.

..  sidebar::

    For example, ``<img src="/images/me.jpg" alt="Me on my bike"/>`` certainly doesn't *look* like a photograph.

They had to do the work, that painful typing of unfamiliar symbols, in one place (a text editor), and could only see the result in another (a web browser).

Just one character wrong, and the result could be nothing. Or, something clearly wrong but that offered no clue about what was wrong, because the error in the output was not an analogue of the error in the input.

..  sidebar::

    In contrast, everything they had done in ICT was about concrete, direct results, in which they could see immediately the effect of something they were doing.


Faith and reward
----------------

It takes a little faith at least to persevere with something without seeing results, when you also don't understand it.

But, the first successful result, just seeing a few lines of HTML turn into a web page, and each successive one was a step upwards in confidence and comprehension - sufficient to get them to the next step.

Amongst the ones who were sufficiently intrigued, it worked to spark rounds of repetition, exploration and experimentation. For some, there was interest at a technical level, the pleasure of seeing it work. At worst, there was at least a dutiful willingness to work through the exercises to get the expected results - they could see *how* web pages were made this way, even if *why* we were doing it like that remained unclear.


Two or three lessons in, one of the bolder ones, who had discovered that all kinds of ideas on how to format things in HTML were only a web search away, showed me his pages. They were liberally sprayed with colours and variations of text size and alignment, all - naturally - applied inline in the HTML.

He'd had a lot of fun learning about it; in fact he had taken his pages home on a USB flash drive, so I was pleased to see how much he had discovered on his own.


"What's the point?"
===================

"That's very nice," I told him, before telling him to remove all of his formatting, and pointing him at the chapter on CSS.

He wasn't at all happy about that. Even after successfully implementing a basic style sheet he was completely underwhelmed by the value he saw for his efforts: "What's the point?"

After some grumbling I was able to persuade him to go on. Ten minutes later I was rewarded with an exclamation: "Woah! Look at that!"

He called me over urgently to show me how he could change everything, on every page on his site, with just one change in his CSS. In the next few minutes he discovered how to use combinations of selectors, and apply classes to elements, visibly astonished and exclaiming at what he had found.

He spent the rest of the lesson just playing with these things and marvelling at what he could do - not at the actual *results*, which made little sense to begin with and grew increasingly wild, but at the *power* he could wield.

He had discovered **abstraction**, and what he could do with it.


Learning abstraction
--------------------

He didn't learn it because I taught it, or because it was explained to him. He learned it by encountering it and exercising its power. My only part in his learning was to get him to do something *that provided a learning experience*.

I wasn't thinking explicitly about abstraction when I created the teaching materials, and the curriculum certainly hadn't mentioned it. I didn't name or discuss abstraction with him. *Abstraction simply wasn't on the agenda at all.*

But, in the space of 20 minutes or so I saw a light come on inside someone's head. A 16-year-old boy left the room equipped with a new concept, that was alive for him *because he had put it to work with his own hands*.

Though he didn't even have a name for it, at that moment abstraction became a new tool at his disposal, for thinking about and acting on the world.

I have no idea whether, in the decades since then, he studied or ever again encountered abstraction in any more formal context. It doesn't really matter. If it's ever needed, the concept is there, in him, ready to be recognised and used in some other situation.


Learning experiences
====================

My career as a high-school teacher was mercifully short, for everyone concerned, and I don't remember it with great pleasure. I remember that episode though: *it was a learning experience of transformative power*, an amazing thing to watch taking place.

I didn't have many experiences of total, unqualified success as a teacher, but that was one of them.

Most remarkable was that it was only the second-most significant learning experience of that lesson. A light came on in *my* head too. It has stayed on ever since and illuminated many things in my life, from teaching philosophy at university to my approach to software documentation and workshops: that **what I explain or say is almost irrelevant, and the only thing that matters is what I get people to do, in order that they learn**.

My aim has to be to deliver *the possibility for a learning experience*, not information or an explanation or a demonstration.

It holds as true for a classroom full of Year 11 pupils in the double period before lunch as it does for a workshop attended by industry professionals. It applies just as firmly to the acquisition of concepts like abstraction as it does to building practical skills.


No more teaching please
=======================

Of course it *is* necessary to do a little bit of telling, showing and explaining (even unasked-for explaining, sometimes) in order to be able to deliver a coherent lesson.

But, it's merely packaging for the lesson, so that the lesson can be delivered. It's not the lesson. It's not the learning experience that is the purpose or the heart of the lesson. What the teacher has to *say* or *show* isn't part of it that matters at all. The packaging is not the value.

Unfortunately it's the part that people wanting to teach get fixated upon, because it's something they can control and because it feels like something they are doing.

----------

Although quite a lot of my life involves "teaching" in some sense or another, I don't really believe it's possible to teach. Every attempt I witness to teach - to deliver knowledge - falls short.

All I can do is offer learners something to do, that contains possibilities for a learning experience, and trust that someone will launch themselves into success from a moment of comprehension that comes out of something they *did*. As a teacher in that instant, all that there really is for me to do is watch it happening.

I learned that lesson myself many years ago. It renews itself repeatedly, in every successful experience I have, and also in the less successful ones, when I forget it, or I am lured into the temptation of trying to teach.
