# Korean
# With `TextMobject`

Using the instructions in this [link](https://www.overleaf.com/learn/latex/Korean) (Korean documents with pdfLaTeX) we deduce that our manimlib / tex_template.tex file should be as follows:

**REMARK**: You must have the CJKutf8 package installed for this method to work, it is usually included in the full versions of LaTeX (MikTeX, TeXLive and MacTeX), if not, it is your task to investigate how it is installed individually, the installation will be different depending on your OS.
```latex
\documentclass[preview]{standalone}

\usepackage[utf8]{inputenc} %<- Instead \usepackage[english]{babel}
\usepackage{CJKutf8} %<- New package from https://www.overleaf.com/learn/latex/Korean
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{dsfont}
\usepackage{setspace}
\usepackage{tipa}
\usepackage{relsize}
\usepackage{textcomp}
\usepackage{mathrsfs}
\usepackage{calligra}
\usepackage{wasysym}
\usepackage{ragged2e}
\usepackage{physics}
\usepackage{xcolor}
\usepackage{microtype}
\DisableLigatures{encoding = *, family = * }
%\usepackage[UTF8]{ctex}
\linespread{1}

\begin{document}

YourTextHere

\end{document}
```

We can see if it works with this scene:

```python
class Korean(Scene):
    def construct(self):
        text = TextMobject(r"""
                \begin{CJK}{UTF8}{}
                \CJKfamily{mj}
                 전체 문서에 대한 기본 정보를 소개 단락.
                 $x^2$
                \end{CJK}
            """)
        self.play(Write(text))
        self.wait()

```

Result:
<p align="center"><img src ="/Idioms/Korean/result.png" /></p>

In order not to have to write so much LaTeX code when we want to write in Korean we can create a new TEX_TEMPLATE. For this, we can add the following to the manimlib/constants.py file:


# In `With` (available for versions from *20/Aug/19* onwards)
See [this](https://github.com/3b1b/manim/pull/680) in the **UTF-8** section.
