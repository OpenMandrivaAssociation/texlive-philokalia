# revision 18651
# category Package
# catalog-ctan /fonts/philokalia
# catalog-date 2007-09-24 10:59:32 +0200
# catalog-license ofl
# catalog-version 1.1
Name:		texlive-philokalia
Version:	1.1
Release:	4
Summary:	A font to typeset the Philokalia Books
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/philokalia
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philokalia.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philokalia.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philokalia.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The philokalia package has been designed to ease the use of the
Philokalia-Regular OpenType font with XeLaTeX. The font started
as a project to digitize the typeface used to typeset the
Philokalia books.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/opentype/public/philokalia/Philokalia-Regular.otf
%{_texmfdistdir}/tex/xelatex/philokalia/eu1plk.fd
%{_texmfdistdir}/tex/xelatex/philokalia/philokalia.sty
%doc %{_texmfdistdir}/doc/xelatex/philokalia/philokalia.pdf
#- source
%doc %{_texmfdistdir}/source/xelatex/philokalia/philokalia.dtx
%doc %{_texmfdistdir}/source/xelatex/philokalia/philokalia.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 754878
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719249
- texlive-philokalia
- texlive-philokalia
- texlive-philokalia
- texlive-philokalia

