# -*- python -*-
# automatically generated wscript

import waflib.Logs as msg

PACKAGE = {
    'name': 'LCG_Interfaces/CLHEP',
    'author': ["ATLAS Collaboration"], 
}

def pkg_deps(ctx):
    ctx.use_pkg("LCG_Configuration")
    ctx.use_pkg("LCG_Settings")
    return

def configure(ctx):
    msg.debug('[configure] package name: '+PACKAGE['name'])

    macro = ctx.hwaf_declare_macro

    config_version = ctx.hwaf_subst_vars("${CLHEP_config_version}").split("-")[0]
    macro("CLHEP_native_version", config_version)

    macro("CLHEP_home", "${LCG_external}/clhep/${CLHEP_config_version}/${LCG_system}")

    macro("CLHEP_incdir", "${CLHEP_home}/include")
    macro("CLHEP_bindir", "${CLHEP_home}/bin")
    macro("CLHEP_libdir", "${CLHEP_home}/lib")

    macro("LIB_CLHEP", (
        {"default": [
            "CLHEP-Cast-${CLHEP_native_version}",
            "CLHEP-Evaluator-${CLHEP_native_version}",
            "CLHEP-Exceptions-${CLHEP_native_version}",
            "CLHEP-GenericFunctions-${CLHEP_native_version}",
            "CLHEP-Geometry-${CLHEP_native_version}",
            "CLHEP-Random-${CLHEP_native_version}",
            "CLHEP-RandomObjects-${CLHEP_native_version}",
            "CLHEP-RefCount-${CLHEP_native_version}",
            "CLHEP-Vector-${CLHEP_native_version}",
            "CLHEP-Matrix-${CLHEP_native_version}",
            ]},
    ))
    
    ctx.hwaf_macro_append("LIB_CLHEP", (
      {"default": ""},
      {"HAS_HEPPDT": "CLHEP-HepPDT-${CLHEP_native_version}"},
    ))

    macro("CLHEP_name", "clhep")

    ctx.hwaf_declare_macro("CLHEP_export_paths", (
      {"default": ["${CLHEP_incdir}", "${CLHEP_libdir}"]},
    ))

    ctx.hwaf_path_prepend('PATH', '${CLHEP_bindir}')

    path = ctx.hwaf_subst_vars('${CLHEP_home}')
    bindir = ctx.hwaf_subst_vars('${CLHEP_bindir}')
    incdir = ctx.hwaf_subst_vars('${CLHEP_incdir}')
    libdir = ctx.hwaf_subst_vars('${CLHEP_libdir}')
    ctx.lcg_declare_external_package(
        'CLHEP',
        path=path,
        libpath=libdir,
        incpath=incdir,
        )
    return

def build(ctx):
    return
