# yiddish-reader
## A project aiming to create high-quality typeset printable Yiddish texts using the TeX typesetting engine and the ConTeXt macro package.


### To compile on Linux:
- Install [ConTeXt Standalone](https://www.contextgarden.net/ConTeXt_Standalone)

- Copy the files in `./context-hack` into `context_dir/tex/texmf-context/tex/context/base/mkiv`

- (optional) Create a shell script to set up the environment and compile. For example:

```
#/bin/bash

source ~/context/tex/setuptex

context reader --jobname=reader-letter --result=reader-letter  --purge
context reader --jobname=reader-book --result=reader-book --mode=book --purge

mv *.pdf ./output
```

Remember to replace `context_dir` with the directory where you installed ConTeXt Standalone.

Thanks to Hans Hagen and Wolfgang Schuster for the quick right-to-left fix. Hopefully it will soon be part of the standard distribution and all this setup won't be necessary.

### Fonts
Fonts are included from [Aharon Varady](https://github.com/aharonium/fonts)'s repository for ease and convenience. Thanks to Aharon, [Culmus Project](http://culmus.sourceforge.net/), and [Michal Sahar](https://github.com/MichalSahar) for the fonts.

### The Texts
Thanks to the [Yiddish Book Center](https://www.yiddishbookcenter.org/) for scanning thousands of Yiddish books and supporting the JOCHRE project for [Yiddish OCR](https://ocr.yiddishbookcenter.org/)!
Thanks to Assaf Urieli for developing [JOCHRE](https://github.com/urieli/jochre)!
Special thanks to [Raphael Finkel](http://www.cs.uky.edu/~raphael/) for making OCR'd texts in Yiddish available before anyone else on the Internet!
