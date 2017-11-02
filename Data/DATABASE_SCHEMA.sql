BEGIN TRANSACTION;
CREATE TABLE `FAKE_DATA` (
	`SENSORID`	INTEGER,
	`TIME`	TEXT,
	`MEAN`	INTEGER,
	`RMS`	INTEGER,
	`CURTOSIS`	INTEGER,
	`SKEWNESS`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "EQUATIONS" (
	`SENSOR_ID`	INTEGER NOT NULL,
	`A1`	INTEGER,
	`B1`	INTEGER,
	`A2`	INTEGER,
	`B2`	INTEGER,
	`A3`	INTEGER,
	`B3`	INTEGER,
	`ALOCAL`	INTEGER,
	`BLOCAL`	INTEGER,
	PRIMARY KEY(`SENSOR_ID`)
);
CREATE TABLE "DATA_SENSOR_PROJECTED_83" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_82" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_81" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_80" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_79" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_78" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_77" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_76" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_75" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_74" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_73" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_72" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_71" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_70" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_69" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_68" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_67" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_66" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_65" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_64" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_63" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_62" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_61" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_60" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_59" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_58" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_57" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_56" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_55" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_54" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_53" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_52" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_51" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_50" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_49" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_48" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_47" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_46" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_45" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_44" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_43" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_42" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_41" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_40" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_39" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_38" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_37" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_36" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_35" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_34" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_33" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_32" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_31" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_30" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_29" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_28" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_27" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_26" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_25" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_24" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_23" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_22" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_21" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_20" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_19" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_18" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_17" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_16" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_15" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_14" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_13" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_12" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_11" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_10" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_09" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_08" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_07" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_06" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_05" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_04" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_03" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_02" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_01" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_PROJECTED_00" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`MEAN_CORRECTED`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`RMS_CORRECTED`	INTEGER NOT NULL
);
CREATE TABLE "DATA_SENSOR_83" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_82" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_81" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_80" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_79" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_78" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_77" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_76" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_75" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_74" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_73" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_72" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_71" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_70" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_69" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_68" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_67" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_66" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_65" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_64" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_63" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_62" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_61" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_60" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_59" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_58" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_57" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_56" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_55" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_54" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_53" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_52" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_51" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_50" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_49" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_48" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_47" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_46" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_45" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_44" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_43" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_42" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_41" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_40" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_39" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_38" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_37" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_36" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_35" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_34" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_33" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_32" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_31" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_30" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_29" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_28" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_27" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_26" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_25" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_24" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_23" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_22" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_21" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_20" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_19" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_18" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_17" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_16" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_15" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_14" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_13" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_12" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_11" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_10" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_09" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_08" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_07" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_06" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_05" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_04" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_03" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_02" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_01" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
CREATE TABLE "DATA_SENSOR_00" (
	`TIME`	TEXT UNIQUE,
	`MEAN`	INTEGER NOT NULL,
	`RMS`	INTEGER NOT NULL,
	`CURTOSIS`	INTEGER NOT NULL,
	`SKEWNESS`	INTEGER NOT NULL,
	`IS_ACCEPTED_FLAG`	INTEGER,
	`RATE`	INTEGER
);
COMMIT;