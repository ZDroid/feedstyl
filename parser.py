#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# Script for displaying pretty RSS feeds
#

from sys import argv
import feedparser

# Data for parse
data = feedparser.parse(argv[1])

# Display core feed data
print "\n\033[1mFeed title:\033[0m", data.feed.title
if "description" in data.feed:
  df = data.feed.description
  if len(df) > 59:
    df = df[:59] + "..."
  print "\033[1mFeed description:\033[0m", df
print "\033[1mFeed URL:\033[0m", data.feed.link

# Display core items data
print "\n\033[1mFeed items:\033[0m\n"
for item in data.entries:
  print "  \033[1mItem title:\033[0m", item.title
  if "description" in item:
    di = item.description
    if len(di) > 55:
      di = di[:55] + "..."
    print "  \033[1mItem description:\033[0m", di
  print "  \033[1mItem link:\033[0m", item.link, "\n"