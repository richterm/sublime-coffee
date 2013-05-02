# Simple CoffeeScript wrapper plugin

This plugin lets you transform CoffeeScript fragments and/ or complete such files from SublimeText 2.

## Requirements

1. NodeJS
2. CoffeeScript package
3. SublimeText 2

## Installation

Clone this repository into your SublimeText 2 Packages/ directory and (re)start SublimeText.

## Usage

Use the `Coffee: Convert` command which is reachable via the context menu or the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P` respectively).
When text is selected it will be send to the CoffeeScript compiler shell command, otherwise the complete file content is transformed.
Either way, the original text is substituted for the transformed JavaScript output.