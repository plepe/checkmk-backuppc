from cmk.gui.i18n import _
from cmk.gui.plugins.metrics import metric_info

metric_info["ageBackup"] = {
    "title": _("Age of last successful backup"),
    "unit": "s",
    "color": "15/a",
}

metric_info["ageFullBackup"] = {
    "title": _("Age of last full backup"),
    "unit": "s",
    "color": "15/a",
}

metric_info["sizeFullBackup"] = {
    "title": _("Size of last full backup"),
    "unit": "bytes",
    "color": "15/a",
}
