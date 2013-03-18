.. _rst-docs:

Github wiki and documentation system 
====================================

Description: Developing a way for CanberraUAV to store it's documentation online

Developers: Chris, Michael

You're looking at it :)

Background:
 * After initially looking at trello.com + google docs, we decided to keep our docs in a DVCS repository for better security (everyone has a copy, no single point of failure).
 * Because it's working well for us already with source code, we decided to publish through GitHub
 * Because we use a lot of python, we decided to go with ReStructured Text / Docutils rather than another markup (such as GitHub flavoured MarkDown, for example)

Notes:
 * See related: :ref:`admin-process-proposal`
 * While GitHub sort-of renders ReStructured text, it doesn't process directives so basically it doesn't work. This is why we automatically publish doc-builds at http://canberrauav.readthedocs.org/
 * Currently only one person has administrator rights to our account at readthedocs.org, this is a pointless risk.
 * At some stage we should review this experiment and decide if we should persevere (shift to :ref:`lessons` or pivot onto another documentation process/system)

.. _admin-process-proposal:

A proposed document management process
--------------------------------------

.. spelling::

   TODAYDATE

The is a bit bureaucratic, but it's an attempt to foster common understanding within the group, *without getting in the way*. It might work as-is, but probably will need to evolve to be successful.

This proposal is related to :ref:`rst-docs`.

The documentation is structured in a way that has an opinion about our management/development process. The pages (representing projects/products/activities) are organised in top level directories based on a model of our "lifecycle". The document generation magic uses the location of the files as information about the status of the project/product/activity.

The top level directories are (currently):
 * in-progress
 * new-ideas-issues
 * on-hold
 * lessons
 * administrivia

The administrivia directory is special, it's a kitchen drawer of stuff that just has to be somewhere.

The first assumption is that the documentation is maintained during or soon after - 8PM Mondays, Canberra time.

Second assumption is that the decision making / information management workflow is similar to the following. First, when a new mumble session starts, the scribe copies administrivia/minutes/minute.rst.template -> administrivia/minutes/TODAYDATE.rst

Then, as each item on the agenda (and for "other business" items that come up):

.. code-block:: sh

   # discuss a project/issue/product/activity, chat chat chat
   # edit/save the minute document
   git add minutes/TODAYDATE.rst;
   git commit -m "minuted topic foo"

Then push the minutes after the session concludes.

Variations include:

.. code-block:: sh

   # discuss new issue/idea/product
   # create file new-ideas-issues/foo.rst
   git add new-ideas-issues/foo.rst;
   git commit -m "documented new issue foo"
   # edit save the minute document
   git add minutes/TODAYDATE.rst;
   git commit -m "minuted new issue foo"

And:


.. code-block:: sh

   # discuss existing issue, decide to change status (e.g. from in-progress to on-hold)
   git mv in-progress/foo.rst on-hold/foo.rst
   # edit/save minutes/TODAYDATE.rst
   git add minutes/TODAYDATE.rst
   git commit -m "change foo from in-progress to on-hold"

What I imagined is that anyone would change the actual contents of the pages at any time (or change their file names), but the locations of the files (and hence the status of the product/issue/activity) would only be changed following open group discussion.

I'm not sure how to decide what's a coarse-grained thing deserving its own page in the documentation, and what's a fine-grained thing that only deserves a github issue (which hopefully would get a mention in the minutes' commit message, hence stay in the loop). Possibly if we try to be sensible it might just work (no specific guidelines).
