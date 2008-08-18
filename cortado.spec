# FIXME: don't bundle all this thirdparty software
# FIXME: do we need to install others jars, besides the applets?

Name:           cortado
Version:        0.2.2
Release:        %mkrel 0.0.1
Epoch:          0
Summary:        Java media framework based on GStreamer's design
Group:          Development/Java
License:        GPLv2+/LGPLv2+/BSD
URL:            http://www.flumotion.net/
Source0:        http://www.flumotion.net/src/cortado/cortado-%{version}.tar.gz
BuildRequires:  ant
BuildRequires:  java-rpmbuild
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Cortado is a Java media framework based on GStreamer's design.

%prep
%setup -q

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant}

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_javadir}

%{__cp} -a output/dist/applet/cortado-ovt-debug-%{version}.jar  %{buildroot}%{_javadir}/%{name}-ovt-%{version}.jar
%{__cp} -a output/dist/applet/cortado-ov-debug-%{version}.jar  %{buildroot}%{_javadir}/%{name}-ov-%{version}.jar
%{__cp} -a output/dist/applet/cortado-mmjs-debug-%{version}.jar  %{buildroot}%{_javadir}/%{name}-mmjs-%{version}.jar

(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc LICENSE.* HACKING README NEWS RELEASE TODO cortado.doap
%{_javadir}/%{name}-ovt-%{version}.jar
%{_javadir}/%{name}-ovt.jar
%{_javadir}/%{name}-ov-%{version}.jar
%{_javadir}/%{name}-ov.jar
%{_javadir}/%{name}-mmjs-%{version}.jar
%{_javadir}/%{name}-mmjs.jar

