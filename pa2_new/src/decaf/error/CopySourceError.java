package decaf.error;

import decaf.Location;

/**
 * example：class 'zig' not found<br>
 * PA2
 */
public class CopySourceError extends DecafError {

	private String source;
	private String target;

	public CopySourceError(Location location, String source, String target) {
		super(location);
		this.source = source;
		this.target = target;
	}

	@Override
	protected String getErrMsg() {
		return "For copy expr, the source " + source + " and the destination " + target + " are not same";
	}

}
