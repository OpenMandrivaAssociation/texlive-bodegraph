%global tl_name bodegraph
%global tl_revision 72949

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Draw Bode, Nyquist and Black plots with gnuplot and TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/bodegraph
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bodegraph.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bodegraph.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides facilities to draw Bode, Nyquist and Black plots
using Gnuplot and Tikz. Elementary Transfer Functions and basic
correctors are preprogrammed for use.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bodegraph
%dir %{_datadir}/texmf-dist/tex/latex/bodegraph
%dir %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot
%dir %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/bodegraph.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/bodegraph.tex
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/10.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/10.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/100.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/100.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/11.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/11.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/12.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/12.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/13.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/13.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/14.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/14.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/15.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/15.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/16.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/16.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/17.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/17.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/18.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/18.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/19.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/19.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/20.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/20.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/21.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/21.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/22.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/22.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/23.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/23.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/24.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/24.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/25.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/25.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/26.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/26.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/27.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/27.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/28.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/28.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/29.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/29.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/3.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/3.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/30.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/30.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/31.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/31.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/32.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/32.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/33.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/33.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/34.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/34.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/35.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/35.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/36.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/36.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/37.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/37.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/38.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/38.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/39.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/39.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/4.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/4.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/40.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/40.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/41.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/41.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/42.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/42.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/43.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/43.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/44.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/44.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/45.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/45.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/46.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/46.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/47.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/47.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/48.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/48.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/49.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/49.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/5.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/5.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/50.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/50.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/51.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/51.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/52.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/52.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/53.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/53.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/54.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/54.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/55.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/55.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/56.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/56.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/57.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/57.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/58.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/58.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/59.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/59.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/6.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/6.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/60.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/60.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/61.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/61.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/62.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/62.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/63.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/63.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/64.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/64.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/65.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/65.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/66.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/66.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/67.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/67.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/68.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/68.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/69.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/69.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/7.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/7.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/71.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/71.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/72.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/72.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/73.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/73.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/74.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/74.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/75.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/75.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/77.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/77.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/78.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/78.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/79.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/79.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/8.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/8.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/80.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/80.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/81.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/81.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/83.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/83.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/84.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/84.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/86.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/86.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/87.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/87.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/88.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/88.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/89.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/89.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/9.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/9.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/90.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/90.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/91.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/91.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/92.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/92.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/94.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/94.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/95.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/95.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/96.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/96.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/98.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/98.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/99.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/99.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/orde1-1.gnuplot
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/gnuplot/bodegraph/orde1-1.table
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/isoa.txt
%doc %{_datadir}/texmf-dist/doc/latex/bodegraph/isom.txt
%{_datadir}/texmf-dist/tex/latex/bodegraph/bodegraph.sty
