%global tl_name sidecap
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7a
Release:	%{tl_revision}.1
Summary:	Typeset captions sideways
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sidecap
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sidecap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sidecap.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sidecap.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines environments called SCfigure and SCtable (analogous to figure
and table) to typeset captions sideways. Options include outercaption,
innercaption, leftcaption and rightcaption.

