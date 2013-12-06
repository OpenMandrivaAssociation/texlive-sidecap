# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sidecap
# catalog-date 2007-01-14 23:54:50 +0100
# catalog-license lppl
# catalog-version 1.6f
Name:		texlive-sidecap
Version:	1.6f
Release:	4
Summary:	Typeset captions sideways
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sidecap
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sidecap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sidecap.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sidecap.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines environments called SCfigure and SCtable (analogous to
figure and table) to typeset captions sideways. Options include
outercaption, innercaption, leftcaption and rightcaption.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sidecap/sidecap.sty
%doc %{_texmfdistdir}/doc/latex/sidecap/README
%doc %{_texmfdistdir}/doc/latex/sidecap/sc-test-common.tex
%doc %{_texmfdistdir}/doc/latex/sidecap/sc-test1.tex
%doc %{_texmfdistdir}/doc/latex/sidecap/sc-test2.tex
%doc %{_texmfdistdir}/doc/latex/sidecap/sc-test3.tex
%doc %{_texmfdistdir}/doc/latex/sidecap/sc-test4.tex
%doc %{_texmfdistdir}/doc/latex/sidecap/sc-test5.tex
%doc %{_texmfdistdir}/doc/latex/sidecap/sc-test6.tex
%doc %{_texmfdistdir}/doc/latex/sidecap/sidecap.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sidecap/Makefile
%doc %{_texmfdistdir}/source/latex/sidecap/sidecap.dtx
%doc %{_texmfdistdir}/source/latex/sidecap/sidecap.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6f-2
+ Revision: 756000
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6f-1
+ Revision: 719532
- texlive-sidecap
- texlive-sidecap
- texlive-sidecap
- texlive-sidecap

