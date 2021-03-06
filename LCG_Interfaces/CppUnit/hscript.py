## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/CppUnit",
    'author': ["ATLAS Collaboration"], 
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("CppUnit_native_version", "${CppUnit_config_version}")
    macro("CppUnit_home", "${LCG_external}/CppUnit/${CppUnit_native_version}/${LCG_system}")

    macro("CppUnit_bindir", "${CppUnit_home}/bin")
    macro("CppUnit_incdir", "${CppUnit_home}/include")
    macro("CppUnit_libdir", "${CppUnit_home}/lib")

    macro("INCLUDES_CppUnit", "${CppUnit_incdir}")
    macro("LIB_CppUnit", (
      {"default": ["cppunit", "dl"]},
      {"target-win": "cppunit_dll"},
    ))
    
    ctx.hwaf_declare_macro("CppUnit_export_paths", (
      {"default": ["${CppUnit_home}/include", "${CppUnit_home}/bin", "${CppUnit_home}/lib"]},
    ))

    ctx.lcg_declare_external_package(
        'CppUnit',
        path='${CppUnit_home}',
        incpath='${CppUnit_incdir}',
        libpath='${CppUnit_libdir}',
        binpath='${CppUnit_bindir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
