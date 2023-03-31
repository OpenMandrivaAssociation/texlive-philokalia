Name:		texlive-philokalia
Version:	45356
Release:	2
Summary:	A font to typeset the Philokalia Books
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/philokalia
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philokalia.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philokalia.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philokalia.source.r%{version}.tar.xz
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
%{_texmfdistdir}/fonts/opentype/public/philokalia
%{_texmfdistdir}/tex/xelatex/philokalia
%doc %{_texmfdistdir}/doc/xelatex/philokalia
#- source
%doc %{_texmfdistdir}/source/xelatex/philokalia

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
