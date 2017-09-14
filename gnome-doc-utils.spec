#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-doc-utils
Version  : 0.20.10
Release  : 6
URL      : http://ftp.gnome.org/pub/GNOME/sources/gnome-doc-utils/0.20/gnome-doc-utils-0.20.10.tar.xz
Source0  : http://ftp.gnome.org/pub/GNOME/sources/gnome-doc-utils/0.20/gnome-doc-utils-0.20.10.tar.xz
Summary  : GNOME Documentation Utilities
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gnome-doc-utils-bin
Requires: gnome-doc-utils-legacypython
Requires: gnome-doc-utils-data
Requires: gnome-doc-utils-locales
Requires: gnome-doc-utils-doc
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : libxml2
BuildRequires : libxml2-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(libxslt)

%description
ABOUT
=====
gnome-doc-utils is a collection of documentation utilities for the Gnome
project.  Notably, it contains utilities for building documentation and
all auxiliary files in your source tree, and it contains the DocBook
XSLT stylesheets that were once distributed with Yelp.  Starting with
Gnome 2.8, Yelp will require gnome-doc-utils for the XSLT.

%package bin
Summary: bin components for the gnome-doc-utils package.
Group: Binaries
Requires: gnome-doc-utils-data

%description bin
bin components for the gnome-doc-utils package.


%package data
Summary: data components for the gnome-doc-utils package.
Group: Data

%description data
data components for the gnome-doc-utils package.


%package dev
Summary: dev components for the gnome-doc-utils package.
Group: Development
Requires: gnome-doc-utils-bin
Requires: gnome-doc-utils-data
Provides: gnome-doc-utils-devel

%description dev
dev components for the gnome-doc-utils package.


%package doc
Summary: doc components for the gnome-doc-utils package.
Group: Documentation

%description doc
doc components for the gnome-doc-utils package.


%package legacypython
Summary: legacypython components for the gnome-doc-utils package.
Group: Default

%description legacypython
legacypython components for the gnome-doc-utils package.


%package locales
Summary: locales components for the gnome-doc-utils package.
Group: Default

%description locales
locales components for the gnome-doc-utils package.


%prep
%setup -q -n gnome-doc-utils-0.20.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505364628
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1505364628
rm -rf %{buildroot}
%make_install
%find_lang gnome-doc-utils

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-doc-prepare
/usr/bin/gnome-doc-tool
/usr/bin/xml2po

%files data
%defattr(-,root,root,-)
/usr/share/gnome-doc-utils/gnome-doc-utils.make
/usr/share/gnome-doc-utils/icons/hicolor/48x48/status/admon-bug.png
/usr/share/gnome-doc-utils/icons/hicolor/48x48/status/admon-caution.png
/usr/share/gnome-doc-utils/icons/hicolor/48x48/status/admon-important.png
/usr/share/gnome-doc-utils/icons/hicolor/48x48/status/admon-note.png
/usr/share/gnome-doc-utils/icons/hicolor/48x48/status/admon-tip.png
/usr/share/gnome-doc-utils/icons/hicolor/48x48/status/admon-warning.png
/usr/share/gnome-doc-utils/icons/hicolor/scalable/status/admon-bug.svg
/usr/share/gnome-doc-utils/icons/hicolor/scalable/status/admon-caution.svg
/usr/share/gnome-doc-utils/icons/hicolor/scalable/status/admon-important.svg
/usr/share/gnome-doc-utils/icons/hicolor/scalable/status/admon-note.svg
/usr/share/gnome-doc-utils/icons/hicolor/scalable/status/admon-tip.svg
/usr/share/gnome-doc-utils/icons/hicolor/scalable/status/admon-warning.svg
/usr/share/gnome-doc-utils/template-document.xml
/usr/share/gnome-doc-utils/template.make
/usr/share/gnome-doc-utils/template.omf.in
/usr/share/gnome-doc-utils/templates/gnome-app-template.xml
/usr/share/gnome-doc-utils/templates/gnome-applet-template.xml
/usr/share/gnome-doc-utils/templates/legal.xml
/usr/share/gnome-doc-utils/watermarks/watermark-blockquote-00AB.png
/usr/share/gnome-doc-utils/watermarks/watermark-blockquote-00BB.png
/usr/share/gnome-doc-utils/watermarks/watermark-blockquote-201C.png
/usr/share/gnome-doc-utils/watermarks/watermark-blockquote-201D.png
/usr/share/gnome-doc-utils/watermarks/watermark-blockquote-201E.png
/usr/share/gnome-doc-utils/watermarks/watermark-code-python.png
/usr/share/gnome-doc-utils/watermarks/watermark-code.png
/usr/share/gnome/help/gnome-doc-make/C/gnome-doc-make.xml
/usr/share/gnome/help/gnome-doc-make/C/legal.xml
/usr/share/gnome/help/gnome-doc-make/C/make-ref.xml
/usr/share/gnome/help/gnome-doc-make/de/gnome-doc-make.xml
/usr/share/gnome/help/gnome-doc-make/de/legal.xml
/usr/share/gnome/help/gnome-doc-make/de/make-ref.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db-chunk.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db-common.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db-label.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db-title.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db-xref.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-autotoc.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-bibliography.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-block.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-callout.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-classsynopsis.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-cmdsynopsis.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-css.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-division.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-ebnf.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-footnote.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-funcsynopsis.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-index.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-info.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-inline.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-l10n.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-list.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-media.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-qanda.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-refentry.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-table.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-title.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html-xref.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2html.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2omf.xml
/usr/share/gnome/help/gnome-doc-xslt/C/db2xhtml.xml
/usr/share/gnome/help/gnome-doc-xslt/C/gettext.xml
/usr/share/gnome/help/gnome-doc-xslt/C/gnome-doc-xslt.xml
/usr/share/gnome/help/gnome-doc-xslt/C/l10n-numbers.xml
/usr/share/gnome/help/gnome-doc-xslt/C/legal.xml
/usr/share/gnome/help/gnome-doc-xslt/C/theme.xml
/usr/share/gnome/help/gnome-doc-xslt/C/translating.xml
/usr/share/gnome/help/gnome-doc-xslt/C/utils.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db-chunk.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db-common.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db-label.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db-title.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db-xref.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-autotoc.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-bibliography.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-block.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-callout.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-classsynopsis.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-cmdsynopsis.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-css.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-division.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-ebnf.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-footnote.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-funcsynopsis.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-index.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-info.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-inline.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-l10n.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-list.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-media.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-qanda.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-refentry.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-table.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-title.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html-xref.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2html.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2omf.xml
/usr/share/gnome/help/gnome-doc-xslt/de/db2xhtml.xml
/usr/share/gnome/help/gnome-doc-xslt/de/gettext.xml
/usr/share/gnome/help/gnome-doc-xslt/de/gnome-doc-xslt.xml
/usr/share/gnome/help/gnome-doc-xslt/de/l10n-numbers.xml
/usr/share/gnome/help/gnome-doc-xslt/de/legal.xml
/usr/share/gnome/help/gnome-doc-xslt/de/theme.xml
/usr/share/gnome/help/gnome-doc-xslt/de/translating.xml
/usr/share/gnome/help/gnome-doc-xslt/de/utils.xml
/usr/share/xml/gnome/xslt/common/theme.xsl
/usr/share/xml/gnome/xslt/common/utils.xsl
/usr/share/xml/gnome/xslt/docbook/common/db-chunk.xsl
/usr/share/xml/gnome/xslt/docbook/common/db-common.xsl
/usr/share/xml/gnome/xslt/docbook/common/db-label.xsl
/usr/share/xml/gnome/xslt/docbook/common/db-title.xsl
/usr/share/xml/gnome/xslt/docbook/common/db-xref.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-autotoc.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-bibliography.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-block.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-callout.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-classsynopsis.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-cmdsynopsis.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-css.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-division.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-ebnf.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-footnote.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-funcsynopsis.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-index.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-info.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-inline.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-l10n.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-list.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-media.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-qanda.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-refentry.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-suppressed.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-table.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-title.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html-xref.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2html.xsl
/usr/share/xml/gnome/xslt/docbook/html/db2xhtml.xsl
/usr/share/xml/gnome/xslt/docbook/omf/db2omf.xsl
/usr/share/xml/gnome/xslt/docbook/utils/chunks.xsl
/usr/share/xml/gnome/xslt/docbook/utils/credits.xsl
/usr/share/xml/gnome/xslt/docbook/utils/figures.xsl
/usr/share/xml/gnome/xslt/docbook/utils/graphics.xsl
/usr/share/xml/gnome/xslt/docbook/utils/ids.xsl
/usr/share/xml/gnome/xslt/gettext/gettext.xsl
/usr/share/xml/gnome/xslt/gettext/l10n-numbers.xsl
/usr/share/xml/gnome/xslt/gettext/l10n.xml
/usr/share/xml/gnome/xslt/mallard/cache/mal-cache.xsl
/usr/share/xml/gnome/xslt/mallard/common/mal-chunk.xsl
/usr/share/xml/gnome/xslt/mallard/common/mal-link.xsl
/usr/share/xml/gnome/xslt/mallard/html/mal2html-block.xsl
/usr/share/xml/gnome/xslt/mallard/html/mal2html-css.xsl
/usr/share/xml/gnome/xslt/mallard/html/mal2html-inline.xsl
/usr/share/xml/gnome/xslt/mallard/html/mal2html-list.xsl
/usr/share/xml/gnome/xslt/mallard/html/mal2html-media.xsl
/usr/share/xml/gnome/xslt/mallard/html/mal2html-page.xsl
/usr/share/xml/gnome/xslt/mallard/html/mal2html-table.xsl
/usr/share/xml/gnome/xslt/mallard/html/mal2html.xsl
/usr/share/xml/gnome/xslt/mallard/html/mal2xhtml.xsl
/usr/share/xml/mallard/1.0/mallard.rnc
/usr/share/xml/mallard/1.0/mallard.rng

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/gnome-doc-utils.pc
/usr/lib64/pkgconfig/xml2po.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files locales -f gnome-doc-utils.lang
%defattr(-,root,root,-)

