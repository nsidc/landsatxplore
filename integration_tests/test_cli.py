"""Tests for CLI."""

from click.testing import CliRunner

from landsatxplore.cli import cli


def test_search():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "search",
            "--dataset",
            "landsat_tm_c1",
            "--location",
            "12.53",
            "-1.53",
            "--start",
            "1995-01-01",
            "--end",
            "1995-12-31",
        ],
    )
    assert result.exit_code == 0
    assert "LT05_L1TP_195051_19950807_20170107_01_T1" in result.output

    
def test_search_pathrow():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "search",
            "--dataset",
            "landsat_8_c1",
            "-PR",
            "34",
            "32",
            "--start",
            "2020-01-20",
            "--end",
            "2020-01-31",
        ],
    )
    assert result.exit_code == 0
    assert "LC08_L1TP_034032_20200124_20200128_01_T1" in result.output
    

def test_download():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ["download", "--dataset", "landsat_tm_c1", "--skip", "LT51950511995219MPS00"],
    )
    assert result.exit_code == 0
    assert "LT05_L1TP_195051_19950807_20170107_01_T1.tar.gz" in result.output
