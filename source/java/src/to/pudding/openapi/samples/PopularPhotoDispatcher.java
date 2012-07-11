package to.pudding.openapi.samples;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;

import to.pudding.openapi.samples.common.OpenApiConnector;

public class PopularPhotoDispatcher {
	
	public static void main ( String []args ) throws MalformedURLException, IOException	{
		OpenApiConnector connector = new OpenApiConnector () ;
		connector.setAccessKey("PUDDING_TO_KEY");		
		connector.setConnectUrl( "http://openapi.pudding.to/api/v1/photos/popular" ) ;
		connector.setCharset("utf-8") ;
		connector.setMethod("POST") ;
		connector.setRequestProperty("User-Agent", "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))");		
		connector.setRequestProperty("Accept", "text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8");
		connector.connect() ;
		
		int code = connector.getResponseCode() ;
		System.out.println ( "code=" + code ) ;
		
		String message = connector.getResponseMessage() ;
		System.out.println ( "message=" + message ) ;
		
		if ( code == HttpURLConnection.HTTP_OK )
		{
			String body = connector.getResponseBody() ;
			System.out.println ( "body=" + body ) ;
		}
	}
}