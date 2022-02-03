# Hash 2 Hash

A _very_ simple script that compares the contents of two directories. No external dependencies required.

This is done by hashing the file contents of both directories in two different hashmaps and checking if one directory is a subset of another.

This was written to help me verify that the files I copied off my Nikon Z6 onto my NAS had the same hash before I deleted them off the camera permanently. However, I realized that Windows makes it very complicated to get the path to a device mounted to the system via MTP (Multimedia Transfer Protocol), so I wasn't able to successfully use this script for my needs.

If at some point it becomes easier to read files off a device mounted via MTP on Windows or I find the motivation to explore how to do it, I will revisit this script.