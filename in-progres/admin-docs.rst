.. _rst-docs:

Github wiki and documentation system 
====================================

Description: Developing a way for CanberraUAV to store it's documentation online

Developers: Chris, Michael

You're looking at it :)

Background:
 * After initially looking at trello.com + google docs, we decided to keep our docs in a DVCS repository forbetter security (everyone has a copy, no single point of failure).
 * Because it's working well for us already with source code, we decided to publish through GitHub
 * Because we use a lot of python, we decided to go with ReStructured Text / Docutils rather than another markup (such as GitHub flavoured MarkDown, for example)

Notes:
 * See related: :ref:`admin-process-proposal`
 * While GitHub sort-of renders ReStructured text, it doesn't process directives so basically it doesn't work. This is why we automatically publish doc-builds at http://canberrauav.readthedocs.org/
 * Currently only one person has admin rights to our account at redthedocs.org, this is a pointless risk.
 * At some stage we should review this experiment and decide if we should persever (shift to :ref:`lessons` or pivot onto another documentation process/system)

