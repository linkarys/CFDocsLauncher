Coldfusion Docs Launcher
=======================

* Provides a command for launching a quick search and launch docs base on current environment
* Quick search anything via input panel

Provides a command for launching a coldfusion 10 quick doc search for the word at the cursor

Fork from [SublimeText2CfQuickDocsLauncher] (<https://github.com/DominicWatson/SublimeText2CfQuickDocsLauncher>)

### Please move to [QuickDocsLauncher] (https://github.com/linkarys/QuickDocsLauncher), This one is combined to [QuickDocsLauncher] (https://github.com/linkarys/QuickDocsLauncher) and is no more under dev.

## Installation

- cd {user sublime folder}/Packages
- git clone https://github.com/linkarys/CFDocsLauncher

## Usage

- Place the cursor around or select the tag/function to be searched/loaded
- Use shift + alt + h to load the doc page for specific tag/function directly
- Use shift + alt+ s  to perform an search operation against specific word
- Use shift + alt + ; to open the quick search panel and use the following syntax to perform search
	```bash
	search engine arg:value [arg:value ...] keyword
	```

	e.g.
	- search keyword array by google:
	```
	array
	```
	- search keyword array by google with language zh:
	```
	g l:zh array
	```
	- search keyword array by python with edition 2.7:
	```
	py e:2.7 array
	```
	- search keyword python array by stackoverflow:
	```
	st python array
	```
All the available abbr for search engine are:
- g or nothing for google
- py for python
- php for php
- st for stackoverflow
- jq for jquery
- mdn for mdn
- subl for sublime text


Quick load and quick search action will detect your environment automatically and load or search the on the proper source.
You Should pre-define the source via Preferences->Package Settings->CF Docs Launcher

## Settings
Here is a demo
```
{
	// The following source will be used when plug-in could not find a specific source base on current environment
	"default": "https://www.google.com/search?q=",

	/**
	 * Use of quick launch and quick search
	 *
	 * doc_url is use for quick launch
	 * search_url is use for quick search
	 * ---------------------------------------------------------------------------
	 */

	"python": {
		"doc_url": "http://docs.python.org/3.4/library/",
		"search_url": "http://docs.python.org/3.4/search.html?check_keywords=yes&area=default&q=",
	},

	/**
	 * Use for quick panel search
	 *
	 * You should defined the source pattern following the following format:
	 *  "prefix": {
	 *  	"pattern": "http://xxxxx/${keyname:defaultValue}/xxxx?q="
	 *  }
	 *
	 *  The when you type in the input panel (ctrl + shift + ; by default) with
	 *  	prefix keyname:val querystring
	 *  It will launch a search at http://xxxxx/var/xxxx?q=querystring
	 *  ---------------------------------------------------------------------------
	 */
	"search_patterns": {
		"g": {
			"pattern": "https://www.google.com/search?hl=${l:en}&q="
		}
	}
}
```
