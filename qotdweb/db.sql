drop table if exists quotes;
create table quotes (
    id integer primary key autoincrement,
    text text not null,
    digest text not null,
    author text not null,
    lastshown integer
);