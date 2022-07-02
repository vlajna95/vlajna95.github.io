public enum Size3 {
    SMALL("s"), MEDIUM("m"), LARGE("l"), EXTRA_LARGE("xl"), UNSPECIFIED("");

    public String code;

    Size(String code) {
        this.code = code;
    }
}
