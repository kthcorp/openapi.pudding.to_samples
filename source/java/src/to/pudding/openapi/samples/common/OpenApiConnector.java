package to.pudding.openapi.samples.common;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.util.Iterator;
import java.util.Properties;

public class OpenApiConnector {
	
	private String connectUrl ;
	private String method ;
	private String charset ;
	private Properties requestProperty ;
	private HttpURLConnection connection ;
	
	private String accessKey ;

	private int responseCode ;
	private String responseMessage ;
	private String responseBody ;
	
	public OpenApiConnector () {
		this.requestProperty = new Properties () ;
	}

	public String getConnectUrl() {
		return connectUrl;
	}

	public void setConnectUrl(String connectUrl) {
		this.connectUrl = connectUrl;
	}

	public String getMethod() {
		return method;
	}

	public void setMethod(String method) {
		this.method = method;
	}

	public String getCharset() {
		return charset;
	}

	public void setCharset(String charset) {
		this.charset = charset;
	}

	public String getAccessKey() {
		return accessKey;
	}

	public void setAccessKey(String accessKey) {
		this.accessKey = accessKey;
	}
	
	public int getResponseCode() {
		return responseCode;
	}
	
	public String getResponseMessage() {
		return responseMessage;
	}

	public String getResponseBody() {
		return responseBody;
	}
	
	public void setRequestProperty(String key, String value) {
		this.requestProperty.put(key, value) ;
	}
	
	public boolean connect () throws MalformedURLException, IOException	{
		
		URL url = new URL (this.connectUrl) ;
		String query = url.getQuery() ;
		
		if ( ( query == null || query.length() == 0 ) && this.accessKey != null ) {
			 query = "access_key=" + this.accessKey ;
		}
		
		if ( this.method.equals("POST") ) {
			connection = (HttpURLConnection) (new URL(this.connectUrl)).openConnection() ;
		}
		else if (this.method.equals("GET")) {
			connection = (HttpURLConnection) (new URL(this.connectUrl + ( query != null ? "?" + query: "") )).openConnection() ;
		}
		else {
			throw new ProtocolException("Invalid HTTP request method: " + this.method);
		}
		
		if ( this.requestProperty != null ) {
			for ( Iterator<Object> it = this.requestProperty.keySet().iterator(); it.hasNext(); ) {
				String key = (String) it.next () ;
				String value = (String) this.requestProperty.get(key) ;
				this.connection.setRequestProperty(key, value);
			}
		}
		
		if ( this.charset != null ) {
			this.connection.setRequestProperty("Accept-Charset", this.charset);
		}
		
		this.connection.setRequestMethod(this.method) ;
		this.connection.setDoOutput(true);
		
		if ( this.method.equals("POST") ) {
			OutputStream os = connection.getOutputStream() ;
			os.write(query.getBytes(this.charset));
			os.flush();
			os.close();
		}
		
		this.responseCode = this.connection.getResponseCode() ;
		this.responseMessage = this.connection.getResponseMessage() ;
		
		if ( this.responseCode == HttpURLConnection.HTTP_OK ) {
			BufferedReader br = new BufferedReader( new InputStreamReader(this.connection.getInputStream()) ) ;
			String line;
			StringBuffer sb = new StringBuffer () ;
			while ( (line = br.readLine()) != null ) {
				sb.append(line);
			}
			
			this.responseBody = sb.toString() ;
		}

		return true ;
	}
}
