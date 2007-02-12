Summary:	'Diffuse program' collection
Summary(pl.UTF-8):   Zestaw 'programów dyfuzji'
Name:		diffuse
Version:	4.1b
Release:	1
License:	Freeware (academic non commercial use)
Group:		Applications
URL:		http://www.uni-wuerzburg.de/mineralogie/crystal/discus/discus.html
Source0:	ftp://www.pa.msu.edu/pub/billinge/discus/Diffuse-%{version}.tar.gz
# Source0-md5:	8b8eccf17e8c98dfbe1a5738b640bb00
Patch0:		%{name}-Makefiles.patch
BuildRequires:	XFree86-devel
BuildRequires:	pgplot-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'Diffuse program' collection contains the following programs:
- DISCUS - Diffuse Scattering & Defect Structure Simulation
%if 0
- PDFFIT - Full Profile Refinement of structural model of the Atomic
           Pair Distribution Function
- KUPLOT - General plotting program (well suited for DISCUS and PDFFIT
           results)
%endif

%description -l pl.UTF-8
Zestaw 'programów dyfuzji' zawiera następujące programy:
- DISCUS - Rozpraszanie dyfuzyjne i symulacja uszkodzonej struktury
%if 0
- PDFFIT - Full Profile Refinement of structural model of the Atomic
           Pair Distribution Function
- KUPLOT - Program do rysowania (dobrze dopasowany do formatu wyników
           DISCUS i PDFFIT)
%endif

%package common
Summary:	Common files for diffuse package
Summary(pl.UTF-8):   Wspólne pliki pakietu diffuse
Group:		Applications

%description common
Common files for diffuse package.

%description common -l pl.UTF-8
Wspólne pliki pakietu diffuse.

%package discus
Summary:	Crystal structure simulation and analysis
Summary(pl.UTF-8):   Symulacja i analiza struktur krystalicznych
Group:		Applications
Requires:	%{name}-common = %{version}

%description discus
DISCUS (DIffuse SCattering and defect strUcture Simulation) is a
program written to simulate crystal structures and to calculate the
corresponding Fourier transform. The main scope of the program is to
simulate defect structures and thus diffuse scattering. It can,
however, be equally well used for the simulation of perfect
structures, of non crystalline materials and can be used as a very
efficient tool in the teaching of diffraction physics.

%description discus -l pl.UTF-8
DISCUS (DIffuse SCattering and defect strUcture Simulation - dyfuzyjne
rozpraszanie i symulacja uszkodzonej struktury) jest programem
napisanym w celu symulacji struktur krystalicznych i obliczania
związanych z nimi transformat Fouriera. Głównym zakresem działania
programu jest symulacja uszkodzonych struktur i ich dyfuzyjnego
rozpraszania. Mimo to program może być używany także do symulacji
idealnych struktur, materiałów niekrystalicznych, oraz jako wydajne
narzędzie do nauki fizyki dyfrakcyjnej.

%prep
%setup -q -n Diffuse-%{version}
%patch0 -p1

%build
%{__make} -C discus/prog \
	CFLAGS="-DREADLINE %{rpmcflags}"
%{__make} -C kuplot/prog \
	CFLAGS="-DREADLINE %{rpmcflags}"
%{__make} -C pdffit/prog \
	CFLAGS="-DREADLINE %{rpmcflags}"

cd pdffit/tools
g77 %{rpmcflags} asc2sbin.f -o asc2sbin
g77 %{rpmcflags} inp2stru.f -o inp2stru
g77 %{rpmcflags} sbin2asc.f -o sbin2asc

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -C discus/prog \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install -C kuplot/prog \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install -C pdffit/prog \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/color.map
%dir %{_datadir}/%{name}/mac

%files discus
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/discus
%{_datadir}/%{name}/discus.hlp
%{_datadir}/%{name}/mac/discus
