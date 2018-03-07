package decaf.error;

import decaf.Location;

/**
 * example：function 'gotoMars' expects 1 argument(s) but 3 given<br>
 * PA2
 */
public class CaseCondError extends DecafError {

	private String type;

	public CaseCondError(Location location, String type) {
		super(location);
		this.type = type;
	}

	@Override
	protected String getErrMsg() {
		return "incompatible case expr: " + type + " given, but int expected";
	}
}
