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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides facilities to draw Bode, Nyquist and Black plots
using Gnuplot and Tikz. Elementary Transfer Functions and basic
correctors are preprogrammed for use.

