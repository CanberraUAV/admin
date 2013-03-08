A propsed document management process
=====================================

The is a bit beurocratic, but it's an attempt to foster common understanding within the group, *without getting in the way*. It might work as-is, but probably will need to evolve to be successful.

The documentation is structured in a way that has an opinion about our management/development process. The pages (representing projects/products/activities) are organised in top level directories based on a model of our "lifecycle". The document generation magic uses the location of the files as information about the status of the project/product/activity.

The top level directories are (currently):
 * in-progres
 * new-ideas-issues
 * on-hold
 * lessons
 * administrivia

The administrivia directory is special, it's a kichen draw of stuff that just has to be somewhere.

The first assumption is that the documentation is maintained during or soon after - 8PM Mondays, Canberra time.

Second assumption is that the decision making / information management workflow is similar to the following. First, when a new mumble session starts, the scribe coppies administrivia/minutes/minute.rst.template -> administrivia/minutes/TODAYDATE.rst

Then, as each item on the agenda (and for "other business" items that come up):

1. discuss a project/issue/product/activity, chat chat chat
2. edit/save the minute document
3. git add minutes/TODAYDATE.rst; git commit -m "minuted topic foo"

Then push the minutes after the session concludes.

Variations include:

1. discuss new issue/idea/product
2. create file new-ideas-issues/foo.rst
3. git add new-ideas-issues/foo.rst; git commit -, "documented new issue foo"
4. edit save the minute document
5. git add minutes/TODAYDATE.rst; git commit -m "minuted new issue foo"

And:

1. discuss existing issue, decide to change status (e.g. from in-proges to on-hold)
2. git mv in-progres/foo.rst on-hold/foo.rst
3. edit/save minutes/TODAYDATE.rst
4. git add minutes/TODAYDATE.rst
5. git commit -m "change foo from in-progres to on-hold"

What I imagined is that anyone would change the actual contents of the pages at any time (or change their file names), but the locations of the files (and hence the status of the product/issue/activity) would only be changed following open group discussion.

I'm not sure how to decide what's a coarse-grained thing deserving it's own page in the documentation, and what's a fine-grained thing that only deserves a github issue (which hopefully would get a mention in the minutes' commit message, hence stay in the loop). Possibly if we try to be sensible it might just work (no specific guidelines).
