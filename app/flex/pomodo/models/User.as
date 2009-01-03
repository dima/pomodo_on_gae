package pomodo.models {
  import org.ruboss.collections.ModelsCollection;
  import org.ruboss.models.RubossModel;
  
  [Resource(name="users")]
  [Bindable]
  public class User extends RubossModel {
    public static const LABEL:String = "login";

    public var login:String = "";

    public var firstName:String = "";

    public var lastName:String = "";

    public var email:String = "";

    [HasOne]
    public var note:Note;
    
    [HasMany]
    public var tasks:ModelsCollection;
    
    [HasMany]
    public var projects:ModelsCollection;
    
    [HasMany]
    public var locations:ModelsCollection;
    
    public function User() {
      super(LABEL);
    }
  }
}
