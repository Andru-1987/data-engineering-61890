DROP TABLE IF EXISTS andru_ocatorres_coderhouse.stage_api_github;

CREATE TABLE stage_api_github(

    id VARCHAR(250),
    name VARCHAR(250),
    full_name VARCHAR(250),
    private BOOLEAN,
    html_url VARCHAR(250),
    size VARCHAR(250)
);
