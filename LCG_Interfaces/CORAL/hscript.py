# -*- python -*-

import waflib.Logs as msg

PACKAGE = {
    'name': 'LCG_Interfaces/CORAL',
    'author': ["ATLAS Collaboration"], 
}

def pkg_deps(ctx):
    ctx.use_pkg("LCG_Configuration")
    ctx.use_pkg("LCG_Settings")
    ctx.use_pkg("LCG_Interfaces/Boost", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/uuid", version="v*", public=True)

    ctx.use_pkg("LCG_Interfaces/XercesC")
    ctx.use_pkg("LCG_Interfaces/lfc")
    ctx.use_pkg("LCG_Interfaces/Frontier_Client")
    ctx.use_pkg("LCG_Interfaces/Expat")
    ctx.use_pkg("LCG_Interfaces/mysql")
    ctx.use_pkg("LCG_Interfaces/sqlite")
    ctx.use_pkg("LCG_Interfaces/CppUnit")
    return

def configure(ctx):
    msg.debug('[configure] package name: '+PACKAGE['name'])

    macro = ctx.hwaf_declare_macro
    
    macro("CORAL_native_version", "${CORAL_config_version}")
    macro("CORAL_base", "${LCG_releases}/CORAL/${CORAL_native_version}")
    macro("CORAL_home", "${CORAL_base}/${LCG_platform}")

    macro("CORAL_bindir", "${CORAL_home}/bin")
    macro("CORAL_incdir", (
        {"default":    "${CORAL_base}/include"},
        {"ATLAS-pack": "${CORAL_home}/include"},
    ))
    macro("CORAL_libdir", "${CORAL_home}/lib")
    macro("CORAL_pydir",  "${CORAL_home}/python")

    ctx.hwaf_macro_append('LIB_CORAL', "lcg_CoralBase")

    ctx.hwaf_macro_append('LIB_CORAL', (
        {"default":                       "lcg_CoralBase"},
        {"NEEDS_CORAL_RELATIONAL_ACCESS": ["lcg_CoralBase",
                                           "lcg_CoralKernel", "lcg_RelationalAccess"]},
        {"NEEDS_CORAL_BASE":              "lcg_CoralBase"},
    ))
    
    ctx.hwaf_macro_append('LIB_CORAL-Relational-Access', (
        {"default": ["lcg_CoralKernel", "lcg_RelationalAccess"]},
    ))
    
    ctx.hwaf_path_prepend("PYTHONPATH", "${CORAL_libdir}")
    ctx.hwaf_path_prepend("PYTHONPATH", "${CORAL_pydir}")

    ctx.hwaf_declare_macro("CORAL_export_paths", (
      {"default": ["${CORAL_home}/lib", "${CORAL_base}/include", "${CORAL_home}/python"]},
    ))

    ctx.lcg_declare_external_package(
        'CORAL',
        path='${CORAL_home}',
        binpath="${CORAL_bindir}",
        incpath="${CORAL_incdir}",
        libpath="${CORAL_libdir}",
        )
    return

def build(ctx):
    return
