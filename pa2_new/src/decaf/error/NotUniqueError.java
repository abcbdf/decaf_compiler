package decaf.error;

import decaf.Location;

/**
 * example：'orz' is not a method in class 'Person'<br>
 * PA2
 */
public class NotUniqueError extends DecafError {

	public NotUniqueError(Location location) {
		super(location);
	}

	@Override
	protected String getErrMsg() {
		return "condition is not unique";
	}

}
