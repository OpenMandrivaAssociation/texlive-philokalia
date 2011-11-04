# revision 18651
# category Package
# catalog-ctan /fonts/philokalia
# catalog-date 2007-09-24 10:59:32 +0200
# catalog-license ofl
# catalog-version 1.1
Name:		texlive-philokalia
Version:	1.1
Release:	1
Summary:	A font to typeset the Philokalia Books
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/philokalia
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philokalia.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philokalia.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philokalia.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The philokalia package has been designed to ease the use of the
Philokalia-Regular OpenType font with XeLaTeX. The font started
as a project to digitize the typeface used to typeset the
Philokalia books.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
