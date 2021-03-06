## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Configuration",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Platforms", version="", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    

    macro = ctx.hwaf_declare_macro
    
    ## projects.
    macro("LCG_config_version", "65")
    ctx.msg("LCG", ctx.env["LCG_config_version"])

    macro("COOL_config_version",  "COOL_2_8_19")
    macro("CORAL_config_version", "CORAL_2_3_28")
    macro("RELAX_config_version", "RELAX_1_3_0o")
    macro("ROOT_config_version",  "5.34.10")
    
    ctx.hwaf_declare_tag("ROOT_GE_5_15", content=[])
    ctx.hwaf_declare_tag("ROOT_GE_5_19", content=[])
    
    ctx.hwaf_apply_tag("ROOT_GE_5_15")
    ctx.hwaf_apply_tag("ROOT_GE_5_19")

    ## externals
    macro("AIDA_config_version",              "3.2.1")
    macro("4suite_config_version",            "1.0.2p1")
    macro("bjam_config_version",              "3.1.13")
    macro("blas_config_version",              "20110419")
    macro("Boost_config_version",             "1.53.0")
    macro("Boost_file_version",               "1_53")
    macro("bz2lib_config_version",            "1.0.2")
    macro("CASTOR_config_version", (
      {"default":                             "2.1.13-6"},
      {"target-mac":                          "2.1.9-4"},
    ))
    macro("cernlib_config_version",           "2006a")
    macro("cgsigsoap_config_version",         "1.3.3-1")
    macro("CLHEP_config_version",             (
        {"default":                           "1.9.4.7"},
        {("ATLAS","ATLAS-pack"):              "2.1.2.3"},
        {"ATLAS":                             "2.1.2.3-atl01"},
    ))
    macro("cmake_config_version",             "2.8.9")
    macro("cmt_config_version",               "v1r20p20081118")
    macro("coin3d_config_version",            "3.1.3p2")
    macro("coverage_config_version",          "3.5.2")
    macro("CppUnit_config_version", (
        {"default":                           "1.12.1_p1"},
        {"ATLAS-pack":                        "1.12.1"},
    ))
    macro("cx_oracle_config_version",         "5.1.1")
    macro("david_config_version",             "1_36a")
    macro("dawn_config_version",              "3_88a")
    macro("dcache_client_config_version", (
      {"default":                             "2.47.6-1"},
      {"target-slc5":                         "2.47.5-0"},
    ))
    macro("dcache_srm_config_version",        "1.9.5-23")
    macro("dcap_config_version",              "2.47.6")
    macro("doxygen_config_version",           "1.8.2")
    macro("dpm_config_version",               "1.8.5-1")
    macro("epel_config_version",              "20120618")
    macro("Expat_config_version",             "2.0.1")
    macro("fftw_config_version", (
      {"default":    "3.1.2"},
      {"target-mac": "3.2.2"},
    ))
    macro("Frontier_Client_config_version",   "2.8.7")
    macro("fastjet_config_version",           "3.0.3")
    macro("GCCXML_config_version",            "0.9.0_20120309p2")
    macro("gdb_config_version",               "7.6")
    macro("genshi_config_version",            "0.6")
    macro("gfal_config_version",              "1.13.0-0")
    macro("globus_config_version", (
      {"default":                             "4.0.3-VDT-1.6.0"},
      {"target-slc":                          "4.0.7-VDT-1.10.1"},
    ))
    macro("graphviz_config_version",          "2.28.0")
    macro("gridftp_ifce_config_version",      "2.1.4-2")
    macro("GSL_config_version",               "1.10")
    macro("HepMC_config_version",             "2.06.08")
    macro("HepPDT_config_version",            "2.06.01")
    macro("igprof_config_version",            "5.9.6")
    macro("ipython_config_version",           "0.12.1")
    macro("is_ifce_config_version",           "1.13.0-0")
    macro("javasdk_config_version",           "1.6.0")
    macro("javajni_config_version",           "${javasdk_config_version}")
    macro("json_config_version",              "2.5.2")
    macro("kcachegrind_config_version",       "0.4.6")
    macro("lapack_config_version",            "3.4.0")
    macro("lcgdmcommon_config_version",       "1.8.5-1")
    macro("lcginfosites_config_version",      "2.6.2-1")
    macro("lcgutils_config_version",          "1.13.0-0")
    macro("lcov_config_version",              "1.9")
    macro("lfc_config_version",               "1.8.5-1")
    macro("libsvm_config_version",            "2.86")
    macro("libtool_config_version", (
      {"default":                             "1.5.26"},
      {"target-slc6":                         "2.4.2"},
    ))
    macro("libunwind_config_version",         "5c2cade")
    macro("lxml_config_version",              "2.3")
    macro("matplotlib_config_version",        "1.1.0")
    macro("minuit_config_version",            "5.27.02")
    macro("mock_config_version",              "0.8.0")
    macro("multiprocessing_config_version",   "2.6.2.1")
    macro("myproxy_config_version", (
      {"default": "3.6-VDT-1.6.0"},
      {"target-slc": "4.2-VDT-1.10.1"},
    ))
    macro("mysql_config_version",             "5.5.14")
    macro("mysql_python_config_version",      "1.2.3")
    macro("neurobayes_config_version",        "3.7.0")
    macro("neurobayes_expert_config_version", "3.7.0")
    macro("nose_config_version",              "1.1.2")
    macro("numpy_config_version",             "1.6.1")
    macro("oracle_config_version",            "11.2.0.3.0")
    macro("processing_config_version",        "0.52")
    macro("py_config_version",                "1.4.8")
    macro("py2neo_config_version",            "1.4.6")
    macro("pydot_config_version",             "1.0.28")
    macro("pyanalysis_config_version",        "1.4")
    macro("pygraphics_config_version",        "1.4")
    macro("pygsi_config_version",             "0.5")
    macro("pylint_config_version",            "0.26.0")
    macro("pyminuit_config_version",          "0.0.1")
    macro("pytest_config_version",            "2.2.4")
    macro("pytools_config_version",           "1.8")
    macro("Python_config_version", (
        {"default":                           "2.7.3"},
        {"target-gcc48":                      "2.7.4"},
    ))
    macro("Python_config_version_twodigit",   "2.7")
    macro("pyqt_config_version",              "4.9.5")
    macro("pyparsing_config_version",         "1.5.6")
    macro("pyxml_config_version",             "0.8.4p1")
    macro("QMtest_config_version",            "2.4.1")
    macro("qt_config_version",                "4.8.4")
    macro("qwt_config_version",               "6.0.1")
    macro("readline_config_version",          "2.5.1p1")
    macro("roofit_config_version",            "3.10p1")
    macro("setuptools_config_version",        "0.6c11")
    macro("scipy_config_version",             "0.10.0")
    macro("sip_config_version",               "4.14")
    macro("soqt_config_version",              "1.5.0")
    macro("sqlalchemy_config_version",        "0.7.7")
    macro("sqlite_config_version",            "3070900")
    macro("srm_ifce_config_version",          "1.13.0-0")
    macro("stomppy_config_version",           "3.1.3")
    macro("storm_config_version",             "0.19")
    macro("sympy_config_version",             "0.7.1")
    macro("tbb_config_version",               "41_20121003")
    macro("tcmalloc_config_version",          "1.7p3")
    macro("uuid_config_version",              "1.42")
    macro("valgrind_config_version",          "3.8.0")
    macro("vdt_config_version",               "0.3.2")
    macro("voms_config_version",              "2.0.8-1")
    macro("vomsapic_config_version",          "1.9.17-1")
    macro("vomsapicpp_config_version",        "1.9.17-1")
    macro("vomsapi_noglobus_config_version",  "1.9.17-1")
    macro("vomsclients_config_version",       "1.9.17-1")
    macro("XercesC_config_version",           "3.1.1p1")
    macro("xqilla_config_version",            "2.2.4p1")
    macro("xrootd_config_version",            "3.2.7")
    
    return # configure


def build(ctx):
    return # build

## EOF ##
