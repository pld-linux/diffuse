Name:		diffuse
Summary:	No summary
Version:	4.1b
Release:	1
Group:		Applications
URL:		http://www.uni-wuerzburg.de/mineralogie/crystal/discus/discus.html
Source0:	ftp://www.pa.msu.edu/pub/billinge/discus/Diffuse-%{version}.tar.gz
Patch0:		%{name}-Makefiles.patch
License:	Freeware (academic non commercial use)
BuildRequires:	readline-devel
BuildRequires:	pgplot-devel
BuildRequires:	XFree86-devel
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%package discus
Summary:	Crystal structure simulation and analysis
Summary(pl):	Symulacja i analiza struktur krystalicznych
Group:		Applications

%description discus
DISCUS (DIffuse SCattering and defect strUcture Simulation) is a
program written to simulate crystal structures and to calculate the
corresponding Fourier transform. The main scope of the program is to
simulate defect structures and thus diffuse scattering. It can,
however, be equally well used for the simulation of perfect
structures, of non crystalline materials and can be used as a very
efficient tool in the teaching of diffraction physics. 

%prep
%setup -q -n Diffuse-%{version}
%patch0 -p1

%build
cd discus/prog
%{__make} CFLAGS="-DREADLINE %{optflags}"
cd ../../kuplot/prog
%{__make} CFLAGS="-DREADLINE %{optflags}"
cd ../../pdffit/prog
%{__make} CFLAGS="-DREADLINE %{optflags}"
cd ../tools
g77 asc2sbin.f -o asc2sbin
g77 inp2stru.f -o inp2stru
g77 sbin2asc.f -o sbin2asc

%install
rm -rf $RPM_BUILD_ROOT
cd discus/prog
%{__make} install DESTDIR=$RPM_BUILD_ROOT
cd ../../kuplot/prog
%{__make} install DESTDIR=$RPM_BUILD_ROOT
cd ../../pdffit/prog
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT
