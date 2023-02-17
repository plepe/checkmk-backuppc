from cmk.gui.i18n import _

from cmk.gui.valuespec import (
    Dictionary,
    Integer,
    TextAscii,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersOperatingSystem,
)

def _item_valuespec_backuppc():
    return TextAscii(title=_("Backup age"))

def _parameter_valuespec_backuppc():
    return Dictionary(
        elements=[
            ("warning_age", Integer(
                title=_("Warning when age of last backup is older than n hours"),
                default_value = 24)
            ),
            ("critical_age", Integer(
                title=_("Critical when age of last backup is older than n hours"),
                default_value = 48)
            ),
        ],
    )

rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="backuppc",
        group=RulespecGroupCheckParametersOperatingSystem,
        match_type="dict",
        item_spec=_item_valuespec_backuppc,
        parameter_valuespec=_parameter_valuespec_backuppc,
        title=lambda: _("Warnings for backupc age"),
    ))
